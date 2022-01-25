from signal import pause
from skimage import io
import numpy as np
import matplotlib.pyplot as plt


def initCentroids(X, K):
    m, n = X.shape
    idx = np.random.choice(m, K)
    centroids = X[idx]
    return np.array(centroids)


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


A = io.imread('bird_small.png')
# print(A.shape)
# plt.imshow(A)
# plt.show()
A = A/255
X = A.reshape(-1, 3)
K = 16
centroids = initCentroids(X, K)
idx, centroids_all = runKmeans(X, centroids, 10)
img = np.zeros(X.shape)
centroids = centroids_all[-1]
for i in range(len(centroids)):
    img[idx == i] = centroids[i]
img = img.reshape(128, 128, 3)
fig, axes = plt.subplots(1, 2, figsize=(12, 6))
axes[0].imshow(A)
axes[1].imshow(img)
plt.show()