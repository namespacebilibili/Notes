from unittest import result
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.optimize as opt


def plot_data(data):
    positive = data[data['Accepted'].isin([1])]
    negative = data[data['Accepted'].isin([0])]
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(positive['Test 1'], positive['Test 2'],
               s=50, c='b', marker='o', label='Accepted')
    ax.scatter(negative['Test 1'], negative['Test 2'],
               s=50, c='r', marker='x', label='Rejected')
    ax.legend()
    ax.set_xlabel('Test 1 Score')
    ax.set_ylabel('Test 2 Score')



def sigmoid(z):
    return 1/(1+np.exp(-z))


def feature_mapping(x1, x2, power):
    data = {}
    for i in np.arange(power+1):
        for p in np.arange(i+1):
            data["f{}{}".format(i-p, p)] = np.power(x1, i-p)*np.power(x2, p)
    return pd.DataFrame(data)


def cost(theta, x, y):
    first = (-y)*np.log(sigmoid(x@theta.T))
    second = (1-y)*np.log(1-sigmoid(x@theta.T))
    return np.mean(first-second)


def costReg(theta, x, y, l=1):
    _theta = theta[1:]
    reg = (l/(2*len(x)))*(_theta@_theta)
    return cost(theta, x, y)+reg


def gradient(theta, x, y):
    return (x.T@(sigmoid(x@theta)-y))/len(x)


def gradientReg(theta, x, y, l=1):
    reg = (l/(len(x)))*theta
    reg[0] = 0
    return gradient(theta, x, y)+reg


def predict(theta, x):
    probability = sigmoid(x@theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]  # return a list


data = pd.read_csv('ex2data2.txt', names=['Test 1', 'Test 2', 'Accepted'])
# print(data.head())
# plot_data(data)

# feature_mapping
x1 = data['Test 1'].values
x2 = data['Test 2'].values
_data = feature_mapping(x1, x2, power=6)  # 28 dims vector
# print (_data.head())
x = _data.values
y = data['Accepted'].values
theta = np.zeros(x.shape[1])
# print(costReg(theta,x,y,l=1))
result = opt.fmin_tnc(func=costReg, x0=theta,
                      fprime=gradientReg, args=(x, y, 2))
theta = result[0]
predictions = predict(theta, x)
correct = [1 if a == b else 0 for (a, b) in zip(predictions, y)]
accuracy = sum(correct)/len(x)
# print(accuracy) 0.8305084745762712
x = np.linspace(-1, 1.5, 250)
xx, yy = np.meshgrid(x, x)

z = feature_mapping(xx.ravel(), yy.ravel(), 6).values
z = z @ theta
z = z.reshape(xx.shape)

plot_data(data)
plt.contour(xx, yy, z, 0)
plt.ylim(-.8, 1.2)
plt.show()