import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt


def sigmoid(z):
    return 1/(1+np.exp(-z))


def cost(theta, x, y):
    first = (-y)*np.log(sigmoid(x@theta.T))
    second = (1-y)*np.log(1-sigmoid(x@theta.T))
    return np.mean(first-second)


def gradient(theta, x, y):
    return (x.T@(sigmoid(x@theta)-y))/len(x)


def predict(theta, x):
    probability = sigmoid(x@theta.T)
    return [1 if x >= 0.5 else 0 for x in probability]  # return a list


data = pd.read_csv('ex2data1.txt', names=['exam1', 'exam2', 'admitted'])
if 'Ones' not in data.columns:
    data.insert(0, 'Ones', 1)

x = data.iloc[:, :-1].values
y = data.iloc[:, -1].values
positive = data[data.admitted.isin([1])]  # 1
negetive = data[data.admitted.isin([0])]  # 0

# fig, ax = plt.subplots(figsize=(6, 5))
# ax.scatter(positive['exam1'], positive['exam2'], c='b', label='Admitted')
# ax.scatter(negetive['exam1'], negetive['exam2'], s=50,
#            c='r', marker='x', label='Not Admitted')
# box = ax.get_position()
# ax.set_position([box.x0, box.y0, box.width, box.height * 0.8])
# ax.legend(loc='center left', bbox_to_anchor=(0.2, 1.12), ncol=3)
# ax.set_xlabel('Exam 1 Score')
# ax.set_ylabel('Exam 2 Score')
# plt.show()

theta = np.zeros(x.shape[1])
result = opt.minimize(fun=cost, x0=theta, args=(x, y),
                      method='TNC', jac=gradient)
# or result=opt.fmin_tnc(func=cost,x0=theta,fprime=gradient,args=(x,y))
# print(result)
theta = result.x
# print(cost(theta, x, y))
predictions = predict(theta, x)
correct = [1 if a == b else 0 for (a, b) in zip(predictions, y)]
accuracy = sum(correct)/(len(x))
# print(accuracy) #0.89

# plot decison boundary
x1 = np.arange(130, step=0.1)
x2 = -(theta[0]+x1*theta[1])/theta[2]
fig, ax = plt.subplots(figsize=(8, 5))
ax.scatter(positive['exam1'], positive['exam2'], c='b', label='Admitted')
ax.scatter(negetive['exam1'], negetive['exam2'], s=50,
           c='r', marker='x', label='Not Admitted')
ax.plot(x1, x2)
ax.set_xlim(0, 130)
ax.set_ylim(0, 130)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_title('Decision Boundary')
plt.show()
