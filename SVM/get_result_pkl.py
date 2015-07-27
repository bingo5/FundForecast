import cPickle as pickle

f1 = file('result_purchase.pkl','rb')
f2 = file('result_redeem.pkl','rb')
ret_purchase = pickle.load(f1)
ret_redeem = pickle.load(f2)
print ret_redeem
f1.close()
f2.close()

f = file('result.pkl','wb')
ret = { }
print len(ret_purchase)
for i in range(30):
    if i not in ret.keys():
        ret[i] = [0,0]
    ret[i][0] = ret_purchase[i + 427]
    ret[i][1] = ret_redeem[i + 427]
pickle.dump(ret,f)
f.close()
print ret
