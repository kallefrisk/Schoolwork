clear
clf

f0 = 10000;
fs = 10000;
N = 64;
t = (0:N-1)/fs;
x = sin(2*pi*f0*t);

plot(t, x, 'o-')
