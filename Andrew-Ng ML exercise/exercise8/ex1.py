import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat


def plotData():
    plt.figure(figsize=(8, 5))
    plt.plot(X[:, 0], X[:, 1], 'bx')
    # plt.show()


def gaussian(X, mu, sigma2):
    m, n = X.shape
    if np.ndim(sigma2) == 1:
        sigma2 = np.diag(sigma2)

    norm = 1./(np.power((2*np.pi), n/2)*np.sqrt(np.linalg.det(sigma2)))
    exp = np.zeros((m, 1))
    # or:
    # e = np.diag(X@np.linalg.inv(sigma2)@X.T)
    # p2 = np.exp(-.5*e)
    for row in range(m):
        xrow = X[row]
        exp[row] = np.exp(-0.5 *
                          ((xrow-mu).T).dot(np.linalg.inv(sigma2)).dot(xrow-mu))
    return norm*exp


def getGaussianParams(X, useMultivariate):
    mu = X.mean(axis=0)
    if useMultivariate:
        sigma2 = ((X-mu).T@(X-mu))/len(X)
    else:
        sigma2 = X.var(axis=0, ddof=0)
    return mu, sigma2


def plotContours(mu, sigma2):
    delta = .3
    x = np.arange(0, 30, delta)
    y = np.arange(0, 30, delta)
    xx, yy = np.meshgrid(x, y)
    points = np.c_[xx.ravel(), yy.ravel()]
    z = gaussian(points, mu, sigma2)
    z = z.reshape(xx.shape)
    cont_levels = [10**h for h in range(-20, 0, 3)]
    plt.contour(xx, yy, z, cont_levels)
    plt.title('Gaussian Contours', fontsize=16)


def selectThreshold(yval, pval):
    def computeF1(yval, pval):
        m = len(yval)
        tp = float(len([i for i in range(m) if pval[i] and yval[i]]))
        fp = float(len([i for i in range(m) if pval[i] and not yval[i]]))
        fn = float(len([i for i in range(m) if not pval[i] and yval[i]]))
        prec = tp/(tp+fp) if (tp+fp) else 0
        rec = tp/(tp+fn) if (tp+fn) else 0
        F1 = 2*prec*rec/(prec+rec) if (prec+rec) else 0
        return F1

    epsilons = np.linspace(min(pval), max(pval), 1000)
    bestF1, bestEpsilon = 0, 0
    for e in epsilons:
        pval_ = pval < e
        thisF1 = computeF1(yval, pval_)
        if thisF1 > bestF1:
            bestF1 = thisF1
            bestEpsilon = e

    return bestF1, bestEpsilon


mat = loadmat('ex8data1.mat')
# print(mat.keys())
X = mat['X']
Xval, yval = mat['Xval'], mat['yval']
# plotData()
# useMV=False
# plotContours(*getGaussianParams(X,useMV))
# plt.show()
# plotData()
# useMV=True
# plotContours(*getGaussianParams(X,useMV))
# plt.show()
mu, sigma2 = getGaussianParams(X, useMultivariate=False)
pval = gaussian(Xval, mu, sigma2)
bestF1, bestEpsilon = selectThreshold(yval, pval)
# print(bestF1,bestEpsilon)
y = gaussian(X, mu, sigma2)
xx = np.array([X[i] for i in range(len(y)) if y[i] < bestEpsilon])
plotData()
plotContours(mu, sigma2)
plt.scatter(xx[:, 0], xx[:, 1], s=80, facecolors='none', edgecolors='r')
plt.show()

mat2 = loadmat('ex8data2.mat')
X2 = mat2['X']
Xval2, yval2 = mat2['Xval'], mat2['yval']
mu, sigma2 = getGaussianParams(X2, useMultivariate=False)
ypred = gaussian(X2, mu, sigma2)
yval2pred = gaussian(Xval2, mu, sigma2)
bestF1, bestEpsilon = selectThreshold(yval2, yval2pred)
anoms = [X2[i] for i in range(X2.shape[0]) if ypred[i] < bestEpsilon]
print(bestEpsilon, len(anoms))
