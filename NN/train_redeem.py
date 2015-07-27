#encoding:utf8
import cPickle as pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from pybrain.structure import *
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
import csv

import matplotlib.pyplot as plt


oo = 2
f = file('../data.pkl','rb')
origin_purchase1 = pickle.load(f)
origin_redeem1 = pickle.load(f)
f.close()
origin_redeem = origin_redeem1

#bulid network
fnn = FeedForwardNetwork()

inLayer = LinearLayer(11,name = 'inLayer')
hiddenLayer = SigmoidLayer(5,name = 'hiddenLayer0')
outLayer = LinearLayer(oo,name = 'outLayer')


fnn.addInputModule(inLayer)
fnn.addModule(hiddenLayer)
fnn.addOutputModule(outLayer)

in_to_hidden = FullConnection(inLayer,hiddenLayer)
hidden_to_out = FullConnection(hiddenLayer,outLayer)

fnn.addConnection(in_to_hidden)
fnn.addConnection(hidden_to_out)

fnn.sortModules()

#bulid dataset
DS = SupervisedDataSet(11,oo)
result = []
purchase = []
i = 0
for item in origin_redeem:
    i += 1
    
    if i < 0:
        continue
    purchase.append(origin_redeem[i-1])

for loop in range(15):
    print loop
    mu1 = np.mean(purchase[259:])
    st1 = np.std(purchase[259:])
    print mu1
    Y1 = (purchase - mu1)/st1

    for i in range(len(Y1)):
        if i < 259  or i > len(purchase) - oo:
            continue
        purchase_Y = []
        for j in range(oo):
            purchase_Y.append(Y1[i + j])
        X = [0 for k in range(11)]
        for j in range(7):
            X[j] = Y1[i - j - 1]
    
        for j in range(4):
            X[7 + j] = Y1[i - j*7 - 14]
        DS.addSample(X,purchase_Y)

    X = DS['input']
    Y = DS['target']

    dataTrain,dataTest = DS.splitWithProportion(0.8)
    xTrain, yTrain = dataTrain['input'],dataTrain['target']
    xTest, yTest = dataTest['input'],dataTest['target']


    trainer = BackpropTrainer(fnn,dataTrain,verbose = True,learningrate = 0.01)
    trnerr,valerr = trainer.trainUntilConvergence(maxEpochs = 100)
    out = fnn.activateOnDataset(dataTest)
    i = 0
 
    out = SupervisedDataSet(11,oo)
    temp = [0 for j in range(oo)]
    d = len(purchase)
    test = [0 for j in range(11)]    
    for j in range(5):
        test[j] = Y1[d - j - 1]
    
    for j in range(4):
        test[7 + j] = Y1[d - j*7 - 14]
    out.addSample(test,temp)
    out = fnn.activateOnDataset(out)
    pre_y = out[0]
    for i in range(len(pre_y)):
	pre_y[i] = pre_y[i] * st1 + mu1
        purchase.append(pre_y[i])
	result.append(pre_y[i])
    print pre_y
print result


print np.mean(result)
f = file('result_redeem.pkl','wb')
pickle.dump(purchase,f)
f.close()
plt.figure(1)
plt.plot(result[:30],'r-*')
#plt.plot(origin_purchase1[397:427],'b-o')
plt.show()

   

            






