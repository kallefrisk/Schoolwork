clear
format long

f = @(x) x.^3 - 2;
g = @(x) x.^3 - 3;
h = @(x) x.^3 - 5;

x = -1:0.01:4;

tol = 10^(-8);

figure(1)
plot(x, zeros(length(x)))
hold on
plot(x, f(x))
hold off

figure(2)
plot(x, zeros(length(x)))
hold on
plot(x, g(x))
hold off

figure(3)
plot(x, zeros(length(x)))
hold on
plot(x, h(x))
hold off

[root_a, n] = bisection(1, 2, tol, f)
[root_b, n] = bisection(1, 2, tol, g)
[root_c, n] = bisection(1, 2, tol, h)