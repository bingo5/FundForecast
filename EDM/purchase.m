filename = 'C:\Users\zhao\Desktop\����\total_data.xls';
DATA1 = xlsread(filename,'A1:A427');
y1 = DATA1(300:427);
y1 = DATA1;
mu1 = mean(y1);
st1 = std(y1);
mu1
st1
Y1 = (y1 - mu1)/st1;
[imf,o,n] = emd(Y1);
figure(1);
hold on;

Y2 = zeros(size(Y1));
Y2 = sum(imf);
plot(Y1);

m = size(imf,1);
figure(2);
hold on;
for i = 1:m
    subplot(m,1,i);
    plot(imf(i,:));
end
figure(3);
hold on 
plot( imf(4,:) + imf(3,:)) ;
purchase = imf';
xlswrite('6��4��\purchase.xls',purchase);

