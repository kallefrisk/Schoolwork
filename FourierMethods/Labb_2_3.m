clear
clf

N=1024;
N1=1024*8;
fs=10000;
Ts=1/fs;
t=(0:N-1)'*Ts; % discrete time samples
f0=1200; % frequency of sinusiod (Hz)
f1=1500; % frequency of sinusoid (Hz)
x=sin(2*pi*f0*t)+10^(-100/20).*sin(2*pi*f1*t); % sampling two sinusoids
X=fft(x);
X1=fft(x, N1);

figure(1)
plot((0:N/2)*fs/N,20*log10(abs(X(1:N/2+1))),'--')
hold on
plot((0:N/2)*fs/N,20*log10(abs(X(1:N/2+1))),'o')
hold off
xlabel('Frekvens f (Hz)')
ylabel('abs(X) (dB)')
title('Amplitudspektrum')

figure(2)
plot((0:N1/2)*fs/N1,20*log10(abs(X1(1:N1/2+1))),'--')
hold on
plot((0:N/2)*fs/N,20*log10(abs(X(1:N/2+1))),'o')
axis([0 fs/2 -50 50])
hold off
xlabel('Frekvens f (Hz)')
ylabel('abs(X) (dB)')
title('Amplitudspektrum')

% DFT with window functions
w_1=boxcar(N); % Rectangular window
w_2=hanning(N); % Hanning window
w_3=hamming(N); % Hamming window
w_4=blackman(N); % Blackman window
w_5=kaiser(N,20); % Kaiser window
Xw=fft(x.*w_5,N1);

figure(3)
plot((0:N1/2)*fs/N1,20*log10(abs(Xw(1:N1/2+1))),'-')
axis([0 fs/2 -200 50])
xlabel('Frekvens f (Hz)')
ylabel('abs(X) (dB)')
title('Amplitudspektrum')