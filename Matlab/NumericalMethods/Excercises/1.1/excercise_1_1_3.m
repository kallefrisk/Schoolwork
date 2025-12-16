clear
format long

% Find all roots of the functions by plotting and bisection

f = @(x) 2*x.^3 - 6*x -1;

g = @(x) exp(x - 2) + x.^3 - x;

h = @(x) 1 + 5*x - 6*x.^3 - exp(2*x);

x = -3:0.01:3;

tol = 10^(-6);

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

[root_a_1, n] = bisection(-2, -1, tol, f)
[root_a_2, n] = bisection(-1, 0, tol, f)
[root_a_3, n] = bisection(1, 2, tol, f)

[root_b_1, n] = bisection(-2, -1, tol, g)
[root_b_2, n] = bisection(-0.5, 0.5, tol, g)
[root_b_3, n] = bisection(0.5, 1.5, tol, g)

[root_c_1, n] = bisection(-1.5, -0.5, tol, h)
[root_c_2, n] = bisection(-0.6, 0.4, tol, h)
[root_c_3, n] = bisection(0.4, 1.4, tol, h)