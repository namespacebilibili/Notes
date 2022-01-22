import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from scipy.io import loadmat
from sklearn import svm


def plotData(X, y):
    plt.figure(figsize=(8, 5))
    plt.scatter(X[:, 0], X[:, 1], c=y.flatten(), cmap='rainbow')
    plt.xlabel('x1')
    plt.ylabel('x2')


def gaussKernel(x1, x2, sigma):
    return np.exp(-((x1-x2)**2).sum()/(2*sigma**2))


def plotBoundary(clf, X):
    x_min, x_max = X[:, 0].min()*1.2, X[:, 0].max()*1.1
    y_min, y_max = X[:, 1].min()*1.2, X[:, 1].max()*1.1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500),
                         np.linspace(y_min, y_max, 500))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z)


mat = loadmat('ex6data2.mat')
X2 = mat['X']
y2 = mat['y']
# plotData(X2,y2)
# plt.show()
sigma = 0.1
gamma = np.power(sigma, -2.)/2
clf = svm.SVC(C=1, kernel='rbf', gamma=gamma)
model = clf.fit(X2, y2.flatten())
plotData(X2, y2)
plotBoundary(model, X2)
plt.show()
