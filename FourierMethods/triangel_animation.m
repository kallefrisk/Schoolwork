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

% Triangelvåg
Xt = exp(-1i*omega*Tp/2).*((-4/Tp)*(cos(omega*Tp/2)-1)./(omega.*omega));
zeroindex = find(k==0);
Xt(zeroindex) = Tp/2;

xt = real(Xt.'*F);
xt_punkt = real(sum(Xt .* exp(1i * omega * t_punkt)));

figure(1)
plot(t, xt, 'r-')
hold on
plot(t_punkt, xt_punkt, 'bo', 'MarkerSize', 8, 'LineWidth', 1.5);
hold off
title(['Iteration N = ', num2str(N)]);
xlabel('t');
ylabel('x_k(t)');

pause(0.1);

end