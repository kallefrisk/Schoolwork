clear
for N = 1:100

% Basic konstanter
T = 1;
Tp = 0.5;
t = -T/2:0.0001:T/2;
t_punkt = 0.03;
% N = 1000;
k = (-N:N)';
omega = 2*pi/T*k;
F = exp(1i*omega*t);

% Kvadratvåg
Xk = Tp/T * exp(-1i*omega*Tp/2) .* (sin(omega*Tp/2) ./ (omega*Tp/2));
zeroindex = find(k==0);
Xk(zeroindex) = Tp;

xk = real(Xk.'*F);
xk_punkt = real(sum(Xk .* exp(1i * omega * t_punkt)));

figure(1)
plot(t, xk, 'r-')
hold on
plot(t_punkt, xk_punkt, 'bo', 'MarkerSize', 8, 'LineWidth', 1.5);
hold off
title(['Iteration N = ', num2str(N)]);
xlabel('t');
ylabel('x_k(t)');

pause(0.1);

end