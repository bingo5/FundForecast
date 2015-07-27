% Power spectral density estimation example
%
clear; clc;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Generate a signal composed of five closely spaced frequencies
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
n         = 512;          % Number of samples
fs        = 1;            % Sampling frequency
nT        = [1:1/fs:n]';  % Time axis
Nf        = 5;            % Number of frequencies
fftlength = 512;          % FFT length used on spectral estimation

f = zeros(Nf,1);
f(1) = 0.05; f(2) = 0.06; f(3) = 0.07; f(4) = 0.08; f(5) = 0.09;
fw      = 2*pi*f;

% Covariance matrix is only well defined for a noisy model
y = randn(n,1); %first signal

for i = 1:Nf
    y  = y + cos(fw(i)*nT);
end
filename = 'C:\Users\zhao\Desktop\Êý¾Ý\total_data.xls';
DATA = xlsread(filename,'B2:B428');
figure;
plot(DATA);
size(DATA)
y = DATA(300:427);
mu = mean(y);
st = std(y);
y = (y - mu)/st;

M = 16;
L = 128 - M + 1;

% Obtain a hankel matrix of y
Y = hankel(y,y);
Y = Y(1:M,1:L);

aL = zeros(L,1);
aM = zeros(M,1);

l = 0:L-1;
m = 0:M-1;

k = [1/fftlength:1/fftlength:0.5];

Smafi = zeros(1,length(k));

for i = 1:length(k)
    aL(:) = exp(2*pi*k(i)*j*l');
    aM(:) = exp(2*pi*k(i)*j*m');

    gW = (1/L) * Y * conj(aL);
    phi = ((1/L) * Y * Y') - gW*gW';

    Smafi(1,i) = (aM' * inv(phi) * gW) / (aM' * inv(phi) * aM);
end
figure;
plot(k,abs(Smafi),'b-o');
title('APES method');
ret = abs(Smafi);
% [a b ]= find(ret== max(ret(200:size(k,2) )))
[num,val] = sort(ret)

r = round(ones(size(k))./k(val))

result = zeros(fftlength,1);

for i = 1:size(r,2)
    if result(r(i)) < num(i) && r(i) < 45 && num(i) > 0.12
        result(r(i)) = num(i)
    end
end
[value,index] = sort(result);
value = value/sum(value)



