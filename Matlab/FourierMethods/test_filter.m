% Butterworth filter
N=20; % Filterordning
Wn=10; % Cut-off (3 dB) i rad/sek
[B,A]=butter(N,Wn,'s');
w=0:0.01:20; % Vinkelfrekvenser i rad/s
H1=freqs(B,A,w);
% Elliptiskt filter
N=5; % Filterordning
Rp=3; % Passbandsrippel (dB)
Rs=40; % Stopbandsrippel (dB)
Wp=10; % Cut-off (Rp dB) i rad/sek
[B,A] = ellip(N,Rp,Rs,Wp,'s');
H2=freqs(B,A,w);
figure(10)
plot(w,20*log10(abs(H1)),'b-')
hold on
plot(w,20*log10(abs(H2)),'k-')
hold off
xlabel('vinkelfrekvens(rad/s)')
legend('Butterworth N=12','Elliptiskt N=5')
title('Amplitudfunktion (dB)')
figure(11)
plot(w,unwrap(angle(H1)),'b-')
hold on
plot(w,unwrap(angle(H2)),'k-')
hold off
xlabel('vinkelfrekvens (rad/s)')
legend('Butterworth N=12','Elliptiskt N=5')
title('Fasfunktion (rad)')