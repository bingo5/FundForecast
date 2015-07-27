library(gdata)
data = read.xls('data.xls',sheet = 1)
y = data$purchase
x = y[259:427]
#x = y[336:427]
library(xts)
Data = xts(x,seq(as.POSIXct("2014-03-01"),len = length(x),by = "day"))
plot(Data)
data_diff1 = diff(Data,differences = 1)
plot(data_diff1)
data_diff2 = diff(Data,differences = 2)
plot(data_diff2)

acf = acf(data_diff2[3:length(x)],lag.max = 100,plot = FALSE)
plot(acf)

pacf = pacf(Data,lag.max = 100,plot = FALSE)
#plot(pacf)
library(forecast)
data.fit = arima(Data,order = c(1,1,2),seasonal = list(order = c(2,0,2),period = 7))
forecast = forecast.Arima(data.fit,h = 30,level = c(99.5))
plot.forecast(forecast)
write.table(forecast$mean,file = "purchase_data.csv",row.names = F,quote = F)

