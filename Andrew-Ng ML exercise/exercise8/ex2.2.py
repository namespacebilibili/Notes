import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat
import scipy.optimize as opt


def normalizeRatings(Y, R):
    Ymean = (Y.sum(axis=1) / R.sum(axis=1)).reshape(-1, 1)
    Ynorm = (Y - Ymean)*R
    return Ynorm, Ymean


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


movies = []
with open('movie_ids.txt', 'r', encoding='ISO-8859-1') as f:
    for line in f:
        movies.append(' '.join(line.strip().split(' ')[1:]))

my_ratings = np.zeros((1682, 1))

my_ratings[0] = 4
my_ratings[97] = 2
my_ratings[6] = 3
my_ratings[11] = 5
my_ratings[53] = 4
my_ratings[63] = 5
my_ratings[65] = 3
my_ratings[68] = 5
my_ratings[182] = 4
my_ratings[225] = 5
my_ratings[354] = 5

for i in range(len(my_ratings)):
    if my_ratings[i] > 0:
        print(my_ratings[i], movies[i])

mat = loadmat('ex8_movies.mat')
Y, R = mat['Y'], mat['R']

Y = np.c_[Y, my_ratings]  # (1682, 944)
R = np.c_[R, my_ratings != 0]  # (1682, 944)
nf = 10
nm, nu = Y.shape
X = np.random.random((nm, nf))
Theta = np.random.random((nu, nf))
l = 10
Ynorm, Ymean = normalizeRatings(Y, R)
params = serialize(X, Theta)
res = opt.minimize(fun=cofiCostFunc,
                   x0=params,
                   args=(Y, R, nm, nu, nf, l),
                   method='TNC',
                   jac=cofiGradient,
                   options={'maxiter': 100})
ret=res.x
fit_X, fit_Theta = deserialize(ret, nm, nu, nf)
pred_mat = fit_X @ fit_Theta.T
pred = pred_mat[:, -1] + Ymean.flatten()
pred_sorted_idx = np.argsort(pred)[::-1]  
print("Top recommendations for you:")
for i in range(10):
    print('Predicting rating %0.1f for movie %s.'
          % (pred[pred_sorted_idx[i]], movies[pred_sorted_idx[i]]))

print("\nOriginal ratings provided:")
for i in range(len(my_ratings)):
    if my_ratings[i] > 0:
        print('Rated %d for movie %s.' % (my_ratings[i], movies[i]))
