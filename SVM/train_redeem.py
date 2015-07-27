#encoding:utf8
import cPickle as pickle
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR

f = file('../data.pkl','rb')
origin_purchase = pickle.load(f)
origin_redeem = pickle.load(f)
f.close()


for loop in range(30):
    index = [5,9]
    pre_data= []
    data = [0 for i in range(len(origin_redeem))]
    for k in range(len(index)):
        pre_redeem = [0 for l in range(len(origin_redeem))]
        for i in range(len(origin_redeem)):
            if i < index[k]:continue
            for l in range(index[k]):
                pre_redeem[i] += origin_redeem[i - 1 - l]

        mu = np.mean(pre_redeem)
        st = np.std(pre_redeem)
        for i in range(len(origin_redeem)):
            pre_redeem[i] = (pre_redeem[i] - mu) /st
        pre_data.append(pre_redeem)

    mu = np.mean(origin_redeem)
    st = np.std(origin_redeem)
    for i in range(len(origin_redeem)):
        data[i] = (origin_redeem[i] - mu)/st
    train_x = []
    test_x = []
    train_y = []
    test_y = []
    XX = []
    YY = []
    for i in range(len(origin_redeem)):
        if i < 245:continue
        X = []
        for j in range(len(index)):
            X.append(pre_data[j][i])
	    
        for j in range(4):
            X.append(data[i - j - 4]) 
	
	
        
	X.append(data[i - 28])            
        X.append(data[i - 21])
	X.append(data[i - 14])
        if i > 400:           

            test_x.append(X)
            test_y.append(data[i])
        else:    
        
            train_x.append(X)
            train_y.append(data[i])
	XX.append(X)
        YY.append(data[i])
	
    train_x = np.mat(train_x)
    train_y = np.array(train_y)
    para1 = [12 + i*0.001 for i in range(40)]
    para2 = [0.0001 + i*0.0001 for i in range(40)]
    c = 0
    g = 0
    
    score = float('-inf')
    for i in range(len(para1)):
        for j in range(len(para2)):
            clf = SVR(C = para1[i],gamma = para2[j])
            clf.fit(train_x,train_y)
            if score  < clf.score(test_x,test_y):
                score = clf.score(test_x,test_y)
                print score
                c = para1[i]
                g = para2[j]
    print c,g
    clf = SVR(C = c,gamma = g)
    clf.fit(XX,YY)
    d = len(origin_redeem)
    pre_x = []
    for j in range(len(index)):        
        pre_x.append(pre_data[j][d - 1])
	    
    for j in range(4):        
        pre_x.append(data[d - j - 4])
    
    
    
    pre_x.append(data[d - 28])  
    pre_x.append(data[d - 21])
    pre_x.append(data[d - 14])
    pre_x = np.mat(pre_x)
    pre_y = clf.predict(pre_x)
    print pre_y
    pre_y = pre_y*st + mu
    print pre_y
    origin_redeem.append(pre_y[0])

f = file('result_redeem.pkl','wb')
pickle.dump(origin_redeem,f)
f.close()
            






