import cPickle as pickle
import csv
import MySQLdb



f = file('result.pkl','rb')
result_first = pickle.load(f)
f.close()


print result_first
result_2 = { }
for key in result_first.keys():
    if key not in result_2.keys():
        result_2[key] = [0,0]
    #result_2[key][0] = result_first[key][0] + total_money*0.00013
    result_2[key][0] = result_first[key][0]    
    result_2[key][1] = result_first[key][1]
f2 = file('result_2.pkl','wb')
pickle.dump(result_2,f2)
f2.close()

f1 = file('tc_comp_predict_table.csv','wb')
writer = csv.writer(f1)

for day in result_2.keys():
    dd = day + 1
    ss = "201409"
    if dd < 10:
        ss = ss + '0' + str(dd)
    else:
        ss = ss + str(dd)
    writer.writerow([ss,int(result_2[day][0]),int(result_2[day][1])])
f1.close()

