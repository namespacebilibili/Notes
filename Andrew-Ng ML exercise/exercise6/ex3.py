from statistics import mode
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


mat3 = loadmat('ex6data3.mat')
X3, y3 = mat3['X'], mat3['y']
Xval, yval = mat3['Xval'], mat3['yval']
# plotData(X3,y3)
# plt.show()
Cvalues = (0.01, 0.03, 0.1, 0.3, 1., 3., 10., 30.)
sigmaValues = Cvalues
best_pair, best_score = (0, 0), 0

for C in Cvalues:
    for sigma in sigmaValues:
        gamma=np.power(sigma,-2.)/2
        model=svm.SVC(C=C,kernel='rbf',gamma=gamma)
        model.fit(X3,y3.flatten())
        this_score=model.score(Xval,yval)
        if this_score>best_score:
            best_score=this_score
            best_pair=(C,sigma)

print('best pair={},best score={}'.format(best_pair,best_score))

model=svm.SVC(C=best_pair[0],kernel='rbf',gamma=np.power(best_pair[1],-2.)/2)
model.fit(X3,y3.flatten())
plotData(X3,y3)
plotBoundary(model,X3)
plt.show()

