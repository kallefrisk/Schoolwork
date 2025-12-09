clear
clf

% Evaluating f(x) = sin(2x), x = 0.5
z = 0.5;
y = sin(2*z);
msgbox(['sin(2*0.5) = ', num2str(y)], 'Result')

% Plotting f(x) and g(x) on [-1, 1]
x =  [-1:0.01:1];
f = sin(2*x);
g = exp(-x.^2);

figure(1)
plot(x, f, 'b-')
hold on
plot(x, g, 'r-')
hold off

% Finding zeroes
x = [-5:0.001:10];
h = x-4*sin(2*x)-3-3/80;
line = 0*x;
figure(2)
plot(x, h, 'b-')
hold on
plot(x, line, 'r-')
hold off
