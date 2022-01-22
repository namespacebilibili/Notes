import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
from scipy.io import loadmat
from sklearn import svm
import re
from stemming.porter2 import stem
import nltk
import nltk.stem.porter


def processEmail(email):
    email = email.lower()
    email = re.sub('<[^<>]>', ' ', email)
    email = re.sub('(http|https)://[^\s]*', 'httpaddr', email)
    email = re.sub('[^\s]+@[^\s]+', 'emailaddr', email)
    email = re.sub('[\$]+', 'dollar', email)
    email = re.sub('[\d]+', 'number', email)
    return email


def email2TokenList(email):
    stemmer = nltk.stem.PorterStemmer()
    email = processEmail(email)
    tokens = re.split(
        '[ \@\$\/\#\.\-\:\&\*\+\=\[\]\?\!\(\)\{\}\,\'\"\>\_\<\;\%]', email)
    tokenlist = []
    for token in tokens:
        token = re.sub('[^a-zA-z0-9]', '', token)
        stemmed = stemmer.stem(token)
        if not len(token):
            continue
        tokenlist.append(stemmed)

    return tokenlist


def email2VocabIndices(email, vocab):
    token = email2TokenList(email)
    index = [i for i in range(len(vocab)) if vocab[i] in token]
    return index


def email2FeatureVector(email):
    df = pd.read_table('vocab.txt', names=['words'])
    vocab = df.values
    vector = np.zeros(len(vocab))
    vocab_indices = email2VocabIndices(email, vocab)
    for i in vocab_indices:
        vector[i]=1
    return vector


with open('emailSample1.txt', 'r') as f:
    email = f.read()
    # print(email)

vector=email2FeatureVector(email)
# print('length of vector = {}\nnum of non-zero = {}'.format(len(vector),int(vector.sum())))
mat=loadmat('spamTrain.mat')
X,y=mat['X'],mat['y']
vector=vector.reshape(1,-1)
mat2=loadmat('spamTest.mat')
Xtest,ytest=mat2['Xtest'],mat2['ytest']
clf=svm.SVC(C=0.1,kernel='linear')
clf.fit(X,y.ravel())
predTrain=clf.score(X,y)
predTest=clf.score(Xtest,ytest)
print(predTrain,predTest)
print(clf.predict(vector))
