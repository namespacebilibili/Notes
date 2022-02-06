import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from PIL import Image
from skimage import transform


def load_dataset():
    train_dataset = h5py.File('train_catvnoncat.h5', 'r')
    train_set_x_orig = np.array(train_dataset["train_set_x"])
    train_set_y_orig = np.array(train_dataset["train_set_y"])
    test_dataset = h5py.File('test_catvnoncat.h5', 'r')
    test_set_x_orig = np.array(test_dataset["test_set_x"])
    test_set_y_orig = np.array(test_dataset["test_set_y"])
    classes = np.array(test_dataset["list_classes"])
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


def draw_picture(train_set_x_orig, train_set_y, classes, index):
    plt.imshow(train_set_x_orig[index])
    print("y= "+str(train_set_y[:, index])+",it's a '" +
          classes[np.squeeze(train_set_y[:, index])].decode("utf-8")+"' picture")
    plt.show()


def sigmoid(z):
    return 1/(1+np.exp(-z))


def initialize_with_zeros(dim):
    return np.zeros((dim, 1)), 0


# GRADED FUNCTION: propagate

def propagate(w, b, X, Y):
    m = X.shape[1]
    A = sigmoid(w.T@X + b)
    cost = (-Y*np.log(A) + (Y-1)*np.log(1-A)).sum() / m
    dw = (X@(A-Y).T) / m
    db = (A - Y).mean()
    cost = np.squeeze(cost)
    grads = {"dw": dw,
             "db": db}
    return grads, cost


def optimize(w, b, X, Y, epoch, alpha, print_cost=False):
    costs = []
    for i in range(epoch):
        grads, cost = propagate(w, b, X, Y)
        dw = grads["dw"]
        db = grads["db"]
        w = w-alpha*dw
        b = b-alpha*db
        if i % 100 == 0:
            costs.append(cost)

        if print_cost and i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))

    params = {"w": w, "b": b}
    grads = {"dw": dw, "db": db}
    return params, grads, costs


def predict(w, b, X):
    m = X.shape[1]
    Y_prediction = np.zeros((1, m))
    w = w.reshape(X.shape[0], 1)
    A = sigmoid(w.T@X+b)
    for i in range(A.shape[1]):
        if A[0, i] < 0.5:
            Y_prediction[0, i] = 0
        else:
            Y_prediction[0, i] = 1
    return Y_prediction


def model(X_train, Y_train, X_test, Y_test, epoch=2000, alpha=0.5, print_cost=False):
    w, b = initialize_with_zeros(X_train.shape[0])
    parameters, grads, costs = optimize(
        w, b, X_train, Y_train, epoch, alpha, print_cost)
    w = parameters["w"]
    b = parameters["b"]
    Y_prediction_test = predict(w, b, X_test)
    Y_prediction_train = predict(w, b, X_train)
    print("train accuracy: {} %".format(
         100 - np.mean(np.abs(Y_prediction_train - Y_train)) * 100))
    print("test accuracy: {} %".format(
         100 - np.mean(np.abs(Y_prediction_test - Y_test)) * 100))
    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test,
         "Y_prediction_train": Y_prediction_train,
         "w": w,
         "b": b,
         "learning_rate": alpha,
         "num_iterations": epoch}

    return d


def test(train_set_x, train_set_y, test_set_x, test_set_y, classes):
    d = model(train_set_x, train_set_y, test_set_x, test_set_y,
              epoch=2000, alpha=0.005, print_cost=True)
    # print(d)
    index = 23
    plt.imshow(test_set_x[:, index].reshape((64, 64, 3)))
    print("y = "+str(test_set_y[0, index])+",you predicted that it is a \"" +
          classes[int(d["Y_prediction_test"][0, index])].decode("utf-8")+"\" picture.")
    plt.show()
    costs = np.squeeze(d['costs'])
    plt.plot(costs)
    plt.ylabel('cost')
    plt.xlabel('iterations (pre hundreds)')
    plt.title("Learning rate ="+str(d["learning_rate"]))
    plt.show()


def choose_learning_rate(train_set_x, train_set_y, test_set_x, test_set_y):
    learning_rates = [0.01, 0.001, 0.0001]
    models = {}
    for i in learning_rates:
        print("learning rate is: "+str(i))
        models[str(i)] = model(train_set_x, train_set_y, test_set_x, test_set_y, epoch=1500, alpha=i, print_cost=False)
        print('\n'+"-------------------------------------------------------"+'\n')
    for i in learning_rates:
        plt.plot(models[str(i)]["costs"],label=str(models[str(i)]["learning_rate"]))

    plt.xlabel("iterations")
    plt.ylabel("cost")
    legend=plt.legend(loc='upper center',shadow=True)
    frame=legend.get_frame()
    frame.set_facecolor('0.90')
    plt.show()
        


train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()
# print(train_set_x_orig.shape,train_set_y.shape,test_set_x_orig.shape,test_set_y.shape)
# draw_picture(train_set_x_orig,train_set_y,classes,index=35)
train_set_x_flatten = train_set_x_orig.reshape(train_set_x_orig.shape[0], -1).T
test_set_x_flatten = test_set_x_orig.reshape(test_set_x_orig.shape[0], -1).T
train_set_x = train_set_x_flatten/255
test_set_x = test_set_x_flatten/255
# w, b, X, Y = np.array([[1], [2]]), 2, np.array(
#     [[1, 2], [3, 4]]), np.array([[1, 0]])
# params, grads, costs = optimize(
#     w, b, X, Y, epoch=100, alpha=0.009, print_cost=False)
# print("w = " + str(params["w"]))
# print("b = " + str(params["b"]))
# print("dw = " + str(grads["dw"]))
# print("db = " + str(grads["db"]))

#test(train_set_x, train_set_y, test_set_x, test_set_y,classes)

#choose_learning_rate(train_set_x,train_set_y,test_set_x,test_set_y)
d = model(train_set_x, train_set_y, test_set_x, test_set_y,
          epoch=10000, alpha=0.0005, print_cost=False)
my_image="nocat.jpg"
image=np.array(plt.imread(my_image))
my_image=transform.resize(image,(64,64)).reshape((1,64*64*3)).T
my_predicted_image=predict(d["w"],d["b"],my_image)
plt.imshow(image)
print("y = " + str(np.squeeze(my_predicted_image)) + ", your algorithm predicts a \"" +
      classes[int(np.squeeze(my_predicted_image)), ].decode("utf-8") + "\" picture.")
plt.show()