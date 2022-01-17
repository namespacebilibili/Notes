from email.header import Header
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def computeCost(X, y, theta):
    inner = np.power((X * theta.T - y), 2)
    return np.sum(inner) / (2 * len(X))


def gradientDescent(X, y, theta, alpha, epoch):
    """return theta,cost"""

    temp = np.matrix(np.zeros(theta.shape))
    parameters = int(theta.flatten().shape[1])
    cost = np.zeros(epoch)  # epoch:numbers of iterations
    m = X.shape[0]

    for i in range(epoch):
        temp = theta - (alpha / m) * (X * theta.T - y).T * X
        theta = temp
        cost[i] = computeCost(X, y, theta)

    return theta, cost


def normalEqn(x, y):
    theta = np.linalg.inv(x.T@x)@x.T@y
    return theta


path = 'ex1data2.txt'
data = pd.read_csv(path, names=['Size', 'Bedrooms', 'Price'])
data = (data-data.mean())/data.std()
# print (data.head())
data.insert(0, 'Ones', 1)
cols = data.shape[1]
x = data.iloc[:, 0:cols-1]
y = data.iloc[:, cols-1:cols]
x = np.matrix(x.values)
y = np.matrix(y.values)
theta = np.matrix(np.array([0, 0, 0]))
alpha = 0.01
epoch = 1000
g1, cost = gradientDescent(x, y, theta, alpha, epoch)
# fig, ax = plt.subplots(figsize=(12, 8))
# ax.plot(np.arange(epoch), cost, 'r')
# ax.set_xlabel('Iterations')
# ax.set_ylabel('Cost')
# ax.set_title('Error vs. Training Epoch')
# plt.show()

# normal equation:
g2 = normalEqn(x, y).T
print(g1)
print(g2)
print(computeCost(x, y, g1), ' ', computeCost(x, y, g2))
