import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat
from scipy.optimize import minimize


def load_weight(path):
    data = loadmat(path)
    return data['Theta1'], data['Theta2']


def load_data(path):
    data = loadmat(path)
    X = data['X']
    y = data['y']
    return X, y


def sigmoid(z):
    return 1/(1+np.exp(-z))


theta1, theta2 = load_weight('ex3weights.mat')
X, y = load_data('ex3data1.mat')
y = y.flatten()
X = np.insert(X, 0, values=np.ones(X.shape[0]), axis=1)
a1 = X
z2 = a1@theta1.T
z2 = np.insert(z2, 0, 1, axis=1)
a2 = sigmoid(z2)
z3=a2@theta2.T
a3=sigmoid(z3)
y_pred=np.argmax(a3,axis=1)+1
accuracy=np.mean(y_pred==y)
print('accuracy={}%'.format(accuracy*100)) #97.52%