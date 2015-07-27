filename = 'C:\Users\zhao\Desktop\数据\total_data.xls';
DATA1 = xlsread(filename,'B1:B427');
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
purchase = imf';
xlswrite('6月4日\redeem.xls',purchase);

