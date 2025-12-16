clear
%k = 2;
%for N=k:k:128
% Generate a sampled sinusoid with frequency f0
fs=10000; % sampling rate (Hz)
Ts=1/fs; % sampling interval
N=64; % number of samples
f0=10000*8/64; % frequency of sinusoid (Hz)
t=(0:N-1)'*Ts; % discrete time samples
x=sin(2*pi*f0*t); % sampling a sinusoid
% plot the sinusoid

figure(1)
plot(t,x,'o-')
xlabel('Tid t')
ylabel('x(t)')
title('Uppgift 1: Sinussignal')

% DFT with and without spectral leakage (f0=1200 and f0=1250)
X=fft(x);
% plot the whole DFT spectrum

figure(2)
plot((0:N-1)*fs/N,20*log10(abs(X)),'o')
hold on
plot((0:N-1)*fs/N,20*log10(abs(X)),'--')
hold off
grid on
%xticks(0:(fs/N):10000)
axis([0 fs -10 40])
xlabel('Frekvens f (Hz)')
ylabel('abs(X)')
title('Amplitudspektrum')
% plot the half DFT spectrum
figure(3)
plot((0:N/2)*fs/N,20*log10(abs(X(1:N/2+1))),'o')
hold on
plot((0:N/2)*fs/N,20*log10(abs(X(1:N/2+1))),'--')
hold off
axis([0 fs/2 -50 50])
xlabel('Frekvens f (Hz)')
ylabel('abs(X) (dB)')
title('Amplitudspektrum')

% DFT with zero padding
N1=1024;
X1=fft(x,N1);
% plot the half DFT spectrum

figure(4)
plot((0:N1/2)*fs/N1,20*log10(abs(X1(1:N1/2+1))),'--')
hold on
plot((0:N/2)*fs/N,20*log10(abs(X(1:N/2+1))),'o')
axis([0 fs/2 -50 50])
hold off
xlabel('Frekvens f (Hz)')
ylabel('abs(X) (dB)')
title('Amplitudspektrum')

% return

% DFT with window functions
w_1=boxcar(N); % Rectangular window
w_2=hanning(N); % Hanning window
w_3=hamming(N); % Hamming window
w_4=blackman(N); % Blackman window
w_5=kaiser(N,5); % Kaiser window
Xw=fft(x.*w_1,N1);
%Xw=fft(w_1,N1); % DFT of window function alone
% plot the half DFT spectrum
figure(5)
plot((0:N1/2)*fs/N1,20*log10(abs(Xw(1:N1/2+1))),'-')
axis([0 fs/2 -200 50])
xlabel('Frekvens f (Hz)')
ylabel('abs(X) (dB)')
title('Amplitudspektrum')

%pause(0.2);
%end
