library(gdata)
data = read.xls('data.xls',sheet = 1)
x = data$purchase
dataseries = ts(x[269:427],frequency = 7,start = c(1))
datapre =  HoltWinters(dataseries)
library('forecast')
data_p = forecast.HoltWinters(datapre,h = 30)
plot(data_p,type = 'l')
plot(data_p$mean)
result = data_p$mean
result[5] = 256432820
result[6] = 193606321
result[7] = 126739169
result[8] =  141746925
result[29] =  419666977
result[30] = 292944659
plot(result)
write.table(result,file = "purchase_data.csv",row.names = F,quote = F)



