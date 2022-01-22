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


def plotBoundary(clf, X):
    x_min, x_max = X[:, 0].min()*1.2, X[:, 0].max()*1.1
    y_min, y_max = X[:, 1].min()*1.2, X[:, 1].max()*1.1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500),
                         np.linspace(y_min, y_max, 500))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contour(xx, yy, Z)


mat = loadmat('ex6data1.mat')
# print(mat.keys())
X = mat['X']
y = mat['y']
# plotData(X, y)
# plt.show()
models = [svm.SVC(C, kernel='linear') for C in [1, 100]]
clfs = [model.fit(X, y.ravel()) for model in models]
titles = ['SVM Decision Boundary with C={}(Example Dataset 1)'.format(
    C) for C in [1, 100]]
for model, title in zip(clfs, titles):
    plotData(X, y)
    plotBoundary(model, X)
    plt.title(title)
    plt.show()
