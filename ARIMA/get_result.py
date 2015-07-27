#encoding:utf8
import csv

f1 = file('purchase_data.csv','rb')
reader1 = csv.reader(f1)
reader1.next()

f2 = file('redeem_data.csv','rb')
reader2 = csv.reader(f2)
reader2.next()

purchase = []
redeem = []
for line in reader1:
    [d1] = line
    d2 = float(d1)
    d2 = int(d2)
    purchase.append(d2)
purchase[7] = purchase[6]


for line in reader2:
    [d1] = line
    d2 = float(d1)
    d2 = int(d2)
    redeem.append(d2)
f1.close()
f2.close()
print redeem
redeem[7] = redeem[6]


f = file('tc_comp_predict_table.csv','wb')
writer = csv.writer(f)

for day in range(len(purchase)):
    dd = day + 1
    ss = '201409'
    if dd < 10:
        ss = ss + '0' + str(dd)
    else:
        ss = ss + str(dd)
    writer.writerow([ss,purchase[day],redeem[day]])
f.close()



    

