import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.optimize as opt
from scipy.io import loadmat
from sklearn.metrics import classification_report
from sklearn.preprocessing import OneHotEncoder


def load_mat(path):
    data = loadmat(path)
    X = data['X']
    y = data['y'].flatten()
    return X, y


def plot_100_images(X):
    index = np.random.choice(range(5000), 100)
    images = X[index]
    fig, ax_array = plt.subplots(
        10, 10, sharex=True, sharey=True, figsize=(8, 8))
    for r in range(10):
        for c in range(10):
            ax_array[r, c].matshow(
                images[r*10+c].reshape(20, 20), cmap='gray_r')

    plt.xticks([])
    plt.yticks([])
    plt.show()


def expand_y(y):
    result = []
    for i in y:
        y_array = np.zeros(10)
        y_array[i-1] = 1
        result.append(y_array)
    '''
    # 或者用sklearn中OneHotEncoder函数
    encoder =  OneHotEncoder(sparse=False)  # return a array instead of matrix
    y_onehot = encoder.fit_transform(y.reshape(-1,1))
    return y_onehot
    '''

    return np.array(result)


def load_weight(path):
    data = loadmat(path)
    return data['Theta1'], data['Theta2']


def serialize(a, b):
    return np.r_[a.flatten(), b.flatten()]


def deserialize(seq):
    return seq[:25*401].reshape(25, 401), seq[25*401:].reshape(10, 26)


def sigmoid(z):
    return 1/(1+np.exp(-z))


def feed_forward(theta, X):
    t1, t2 = deserialize(theta)
    a1 = X
    z2 = a1@t1.T
    a2 = np.insert(sigmoid(z2), 0, 1, axis=1)
    z3 = a2@t2.T
    a3 = sigmoid(z3)
    return a1, z2, a2, z3, a3


def cost(theta, X, y):
    a1, z2, a2, z3, h = feed_forward(theta, X)
    J = -y*np.log(h)-(1-y)*np.log(1-h)
    return J.sum()/len(X)
    """
    or:
        J=0
        for i in range(len(X)):
            first = -y[i]*np.log(h[i])
            second = -(1-y[i])*np.log(1-h[i])
            J = J+np.sum(first+second)
        J = J/len(X)
        return J
    """


def regularized_cost(theta, X, y, l=1):
    t1, t2 = deserialize(theta)
    reg = np.sum(t1[:, 1:]**2)+np.sum(t2[:, 1:]**2)
    return l/(2*len(X))*reg+cost(theta, X, y)


def sigmoid_gradient(z):
    return sigmoid(z)*(1-sigmoid(z))


def random_init(size):
    return np.random.uniform(-0.12, 0.12, size)


def gradient(theta, X, y):
    t1, t2 = deserialize(theta)
    a1, z2, a2, z3, h = feed_forward(theta, X)
    d3 = h-y
    d2 = d3@t2[:, 1:]*sigmoid_gradient(z2)
    D2 = d3.T@a2
    D1 = d2.T@a1
    D = (1/len(X))*serialize(D1, D2)
    return D


def regularized_gradient(theta, X, y, l=1):
    D1, D2 = deserialize(gradient(theta, X, y))
    t1[:, 0] = 0
    t2[:, 0] = 0
    reg_D1 = D1+(l/len(X))*t1
    reg_D2 = D2+(l/len(X))*t2
    return serialize(reg_D1, reg_D2)


def gradient_checking(theta, X, y, e):
    def a_numeric_grad(plus, minus):
        return (regularized_cost(plus, X, y, l=1)-regularized_cost(minus, X, y, l=1))/(e*2)

    numeric_grad = []
    for i in range(len(theta)):
        plus = theta.copy()
        minus = theta.copy()
        plus[i] = plus[i]+e
        minus[i] = minus[i]+e
        grad_i = a_numeric_grad(plus, minus)
        numeric_grad.append(grad_i)

    numeric_grad = np.array(numeric_grad)
    analytic_grad = regularized_gradient(theta, X, y, l=1)
    diff = np.linalg.norm(numeric_grad-analytic_grad) / \
        np.linalg.norm(numeric_grad+analytic_grad)
    print('If your backpropagation implementation is correct,\nthe relative difference will be smaller than 10e-9 (assume epsilon=0.0001).\nRelative Difference: {}\n'.format(diff))


def nn_training(X, y):
    init_theta = random_init(10285)
    res = opt.minimize(fun=regularized_cost, x0=init_theta, args=(
        X, y, 1), method='TNC', jac=regularized_gradient, options={'maxiter': 400})
    return res


def accuracy(theta, X, y):
    a, b, c, d, h = feed_forward(res.x, X)
    y_pred = np.argmax(h, axis=1)+1
    print(classification_report(y, y_pred))


def plot_hidden(theta):
    t1, _ = deserialize(theta)
    t1=t1[:,1:]
    fig,ax_array=plt.subplots(5,5,sharex=True,sharey=True,figsize=(6,6))
    for r in range(5):
        for c in range(5):
            ax_array[r,c].matshow(t1[r*5+c].reshape(20,20),cmap='gray_r')
    
    plt.xticks([])
    plt.yticks([])
    plt.show()

X,y=load_mat('ex4data1.mat')
plot_100_images(X)
raw_X, raw_y = load_mat('ex4data1.mat')
X = np.insert(raw_X, 0, 1, axis=1)
y = expand_y(raw_y)
# print(X.shape,y.shape)
t1, t2 = load_weight('ex4weights.mat')
# print(t1.shape,t2.shape)
theta = serialize(t1, t2)
a1, z2, a2, z3, a3 = feed_forward(theta, X)
# print(cost(theta, X, y)) 0.2876291651613189
# print(regularized_cost(theta, X, y, l=1)) 0.38376985909092365
# gradient_checking(theta,X,y,e=0.0001)
# res = nn_training(X, y)
# accuracy(res.x, X, raw_y)
# plot_hidden(res.x)
