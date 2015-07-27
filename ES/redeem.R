library(gdata)
data = read.xls('data.xls',sheet = 1)
x = data$redeem
dataseries = ts(x[269:427],frequency = 7,start = c(1))
datapre =  HoltWinters(dataseries)
library('forecast')
data_p = forecast.HoltWinters(datapre,h = 30)
plot(data_p,type = 'l')

result = data_p$mean
result[5] = 196812800
result[6] = 205186040
result[7] = 140190338
result[8] = 242183302
result[29] = 341945393
result[30] = 224176289
plot(result)
write.table(result,file = "redeem_data.csv",row.names = F,quote = F)



