clear
format long

% Find the root to six decimal places

tol = 10^(-6);

f = @(x) x.^3 -9;

g = @(x) 3*x.^3 +x.^2 - x - 5;

h = @(x) cos(x).^2 - x + 6;

[root_a, n] = bisection(2, 3, tol, f)
[root_b, n] = bisection(1, 2, tol, g)
[root_c, n] = bisection(6, 7, tol, h)