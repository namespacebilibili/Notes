import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat


def serialize(X, Theta):
    return np.r_[X.flatten(), Theta.flatten()]


def deserialize(seq, nm, nu, nf):
    return seq[:nm*nf].reshape(nm, nf), seq[nm*nf:].reshape(nu, nf)


def cofiCostFunc(params, Y, R, nm, nu, nf, l=0):
    X, Theta = deserialize(params, nm, nu, nf)
    error = 0.5*np.square((X@Theta.T-Y)*R).sum()
    reg1 = .5*l*np.square(Theta).sum()
    reg2 = .5*l*np.square(X).sum()
    return error+reg1+reg2


def cofiGradient(params, Y, R, nm, nu, nf, l=0):
    """
    计算X和Theta的梯度，并序列化输出。
    """
    X, Theta = deserialize(params, nm, nu, nf)

    X_grad = ((X@Theta.T-Y)*R)@Theta + l*X
    Theta_grad = ((X@Theta.T-Y)*R).T@X + l*Theta

    return serialize(X_grad, Theta_grad)


def checkGradient(params, Y, myR, nm, nu, nf, l=0.):
    print('Numerical Gradient \t cofiGrad \t\t Difference')
    grad = cofiGradient(params, Y, myR, nm, nu, nf, l)
    e = 0.0001
    nparams = len(params)
    e_vec = np.zeros(nparams)
    for i in range(10):
        idx = np.random.randint(0, nparams)
        e_vec[idx] = e
        loss1 = cofiCostFunc(params-e_vec, Y, myR, nm, nu, nf, l)
        loss2 = cofiCostFunc(params+e_vec, Y, myR, nm, nu, nf, l)
        numgrad = (loss2-loss1)/(2*e)
        e_vec[idx] = 0
        diff = np.linalg.norm(
            numgrad - grad[idx]) / np.linalg.norm(numgrad + grad[idx])
        print('%0.15f \t %0.15f \t %0.15f' % (numgrad, grad[idx], diff))


mat = loadmat('ex8_movies.mat')
# # print(mat.keys())
Y, R = mat['Y'], mat['R']
# nm,nu=Y.shape
# nf=100
# fig = plt.figure(figsize=(8, 8*(1682./943.)))
# plt.imshow(Y, cmap='rainbow')
# plt.colorbar()
# plt.ylabel('Movies (%d)' % nm, fontsize=20)
# plt.xlabel('Users (%d)' % nu, fontsize=20)
# plt.show()
mat = loadmat('ex8_movieParams.mat')
X = mat['X']
Theta = mat['Theta']
nu = int(mat['num_users'])
nm = int(mat['num_movies'])
nf = int(mat['num_features'])
nu = 4
nm = 5
nf = 3
X = X[:nm, :nf]
Theta = Theta[:nu, :nf]
Y = Y[:nm, :nu]
R = R[:nm, :nu]
# print(cofiCostFunc(serialize(X,Theta),Y,R,nm,nu,nf,1.5))
# print("Checking gradient with lambda = 0...")
# checkGradient(serialize(X, Theta), Y, R, nm, nu, nf)
# print("\nChecking gradient with lambda = 1.5...")
# checkGradient(serialize(X, Theta), Y, R, nm, nu, nf, l=1.5)
