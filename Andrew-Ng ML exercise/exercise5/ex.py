import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.optimize as opt
from scipy.io import loadmat


def plotData():
    plt.figure(figsize=(8, 5))
    plt.scatter(X[:, 1:], y, c='r', marker='x')
    plt.xlabel('Change in water level (x)')
    plt.ylabel('Water flowing out of the dam (y)')
    plt.grid(True)
    # plt.show()


def costReg(theta, X, y, l):
    cost = ((X@theta.T-y.flatten())**2).sum()
    regterm = l*(theta[1:]@theta[1:])
    return (cost+regterm)/(2*len(X))


def gradientReg(theta, X, y, l):
    grad = (X@theta-y.flatten())@X
    regterm = l*theta
    regterm[0] = 0
    return (grad+regterm)/len(X)


def trainLinearReg(X, y, l):
    theta = np.zeros(X.shape[1])
    res = opt.minimize(fun=costReg, x0=theta, args=(
        X, y, l), method='TNC', jac=gradientReg)
    return res.x


def plot_learning_curve(X, y, Xval, yval, l):
    xx = range(1, len(X)+1)
    training_cost, cv_cost = [], []
    for i in xx:
        res = trainLinearReg(X[:i], y[:i], l)
        training_cost_i = costReg(res, X[:i], y[:i], l)
        cv_cost_i = costReg(res, Xval, yval, l)
        training_cost.append(training_cost_i)
        cv_cost.append(cv_cost_i)

    plt.figure(figsize=(8, 5))
    plt.plot(xx, training_cost, label='Training Cost')
    plt.plot(xx, cv_cost, label='Cv Cost')
    plt.legend()
    plt.xlabel('Number of training examples')
    plt.ylabel('Error')
    plt.title('Learning Curve for linear regression')
    plt.grid(True)
    plt.show()


def genPolyFeatures(X, power):
    Xpoly = X.copy()
    for i in range(2, power+1):
        Xpoly = np.insert(
            Xpoly, Xpoly.shape[1], np.power(Xpoly[:, 1], i), axis=1)
    return Xpoly


def get_means_std(X):
    means = np.mean(X, axis=0)
    stds = np.std(X, axis=0, ddof=1)
    return means, stds


def featureNormalize(myX, means, stds):
    X_norm = myX.copy()
    X_norm[:, 1:] = X_norm[:, 1:]-means[1:]
    X_norm[:, 1:] = X_norm[:, 1:]/stds[1:]
    return X_norm


def plot_fit(means, stds, l):
    theta = trainLinearReg(X_norm, y, l)
    x = np.linspace(-75, 55, 50)
    xmat = x.reshape(-1, 1)
    xmat = np.insert(xmat, 0, 1, axis=1)
    Xmat = genPolyFeatures(xmat, power)
    Xmat_norm = featureNormalize(Xmat, means, stds)

    plotData()
    plt.plot(x, Xmat_norm@theta, 'b--')


path = 'ex5data1.mat'
data = loadmat(path)
X, y = data['X'], data['y']
Xval, yval = data['Xval'], data['yval']
Xtest, ytest = data['Xtest'], data['ytest']
X = np.insert(X, 0, 1, axis=1)
Xval = np.insert(Xval, 0, 1, axis=1)
Xtest = np.insert(Xtest, 0, 1, axis=1)
# plotData()
# theta = np.ones(X.shape[1])
# print(costReg(theta,X,y,l=1))
# fit_theta = trainLinearReg(X, y, 0)
# plotData()
# plt.plot(X[:,1],X@fit_theta)
# plt.show()
# plot_learning_curve(X, y, Xval, yval, 0)
power = 6
train_means, train_stds = get_means_std(genPolyFeatures(X, power))
X_norm = featureNormalize(genPolyFeatures(X, power), train_means, train_stds)
Xval_norm = featureNormalize(genPolyFeatures(
    Xval, power), train_means, train_stds)
Xtest_norm = featureNormalize(genPolyFeatures(
    Xtest, power), train_means, train_stds)

# plot_fit(train_means,train_stds,100)
# plot_learning_curve(X_norm,y,Xval_norm,yval,100)
# lambdas=[0.,0.001,0.003,0.01,0.03,0.1,0.3,1.,3.,10.]
# errors_train,errors_val=[],[]
# for l in lambdas:
#     theta=trainLinearReg(X_norm,y,l)
#     errors_train.append(costReg(theta,X_norm,y,0))
#     errors_val.append(costReg(theta,Xval_norm,yval,0))

# plt.figure(figsize=(8,5))
# plt.plot(lambdas,errors_train,label='Train')
# plt.plot(lambdas,errors_val,label='Cross Validation')
# plt.legend()
# plt.xlabel('lambda')
# plt.ylabel('Error')
# plt.grid(True)
# plt.show()

theta=trainLinearReg(X_norm,y,3)
print('test cost(l={})={}'.format(3,costReg(theta,Xtest_norm,ytest,0)))


