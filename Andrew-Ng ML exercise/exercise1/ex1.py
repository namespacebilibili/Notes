import numpy as np
import pandas as pd
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


path = 'ex1data1.txt'
data = pd.read_csv(path, header=None, names=['Population', 'Profit'])
# print(data.head())  # visualize data
# data.plot(kind='scatter', x='Population', y='Profit', figsize=(8,5))
# plt.show()
data.insert(0, 'Ones', 1)
cols = data.shape[1]
X = data.iloc[:, 0:cols - 1]
y = data.iloc[:, cols - 1:cols]
X = np.matrix(X.values)
y = np.matrix(y.values)
theta = np.matrix([0, 0])
# print(computeCost(X,y,theta)) 32.072733877455676
alpha = 0.01
epoch = 1000
final_theta, cost = gradientDescent(X, y, theta, alpha, epoch)
print(computeCost(X, y, final_theta))
x = np.linspace(data.Population.min(), data.Population.max(), 100)
f = final_theta[0, 0] + (final_theta[0, 1] * x)
fig, ax = plt.subplots(figsize=(6, 4))
ax.plot(x, f, 'r', label='Prediction')
ax.scatter(data['Population'], data.Profit, label='Training Data')
ax.legend(loc=2)  # 2 means upperleft
ax.set_xlabel('Population')
ax.set_ylabel('Profit')
ax.set_title('Predicted Profit vs. Population Size')
plt.show()
