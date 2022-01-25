import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import loadmat


def findClosestCentroids(X, centroids):
    """
    output a one-dimensional array idx that holds the 
    index of the closest centroid to every training example.
    """
    idx = []
    max_dist = 1000000
    for i in range(len(X)):
        minus = X[i] - centroids  # here use numpy's broadcasting
        dist = minus[:, 0]**2 + minus[:, 1]**2
        if dist.min() < max_dist:
            ci = np.argmin(dist)
            idx.append(ci)
    return np.array(idx)


def computeCentroids(X, idx):
    centroids = []
    for i in range(len(np.unique(idx))):
        u_k = X[idx == i].mean(axis=0)
        centroids.append(u_k)
    return np.array(centroids)


def plotData(X, centroids, idx=None):
    colors = ['b', 'g', 'gold', 'darkorange', 'salmon', 'olivedrab',
              'maroon', 'navy', 'sienna', 'tomato', 'lightgray', 'gainsboro'
              'coral', 'aliceblue', 'dimgray', 'mintcream', 'mintcream']
    assert len(centroids[0]) <= len(colors), 'colors not enough'
    subX = []
    if idx is not None:
        for i in range(centroids[0].shape[0]):
            x_i = X[idx == i]
            subX.append(x_i)
    else:
        subX = [X]

    plt.figure(figsize=(8, 5))
    for i in range(len(subX)):
        xx = subX[i]
        plt.scatter(xx[:, 0], xx[:, 1], c=colors[i], label='Cluster %d' % i)
    plt.legend()
    plt.grid(True)
    plt.xlabel('x1', fontsize=14)
    plt.ylabel('x2', fontsize=14)
    plt.title('Plot of X Points', fontsize=16)
    xx, yy = [], []
    for centroid in centroids:
        xx.append(centroid[:, 0])
        yy.append(centroid[:, 1])
    plt.plot(xx, yy, 'rx--', markersize=8)
    plt.show()


def runKmeans(X, centroids, max_iters):
    K = len(centroids)
    centroids_all = []
    centroids_all.append(centroids)
    centroids_i = centroids
    for i in range(max_iters):
        idx = findClosestCentroids(X, centroids_i)
        centroids_i = computeCentroids(X, idx)
        centroids_all.append(centroids_i)

    return idx, centroids_all


def initCentroids(X, K):
    m, n = X.shape
    idx = np.random.choice(m, K)
    centroids = X[idx]
    return np.array(centroids)


mat = loadmat('ex7data2.mat')
# print(mat.keys())
X = mat['X']
init_centroids = np.array([[3, 3], [6, 2], [8, 5]])
# idx = findClosestCentroids(X, init_centroids)
# print(computeCentroids(X, idx))
# plotData(X,[init_centroids],idx)
# idx, centroids_all = runKmeans(X, init_centroids, 20)
# plotData(X, centroids_all, idx)
for i in range(3):
    centroids=initCentroids(X,3)
    idx,centroids_all=runKmeans(X,centroids,20)
    plotData(X,centroids_all,idx)
    

