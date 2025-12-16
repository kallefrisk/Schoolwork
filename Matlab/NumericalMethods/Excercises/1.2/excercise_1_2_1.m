clear
format long

f = @(x) (2*x + 2).^(1/3);
g = @(x) log(7 - x);
h = @(x) log(4 - sin(x));

[root_a, n] = FPI(1, 1e-8, f)
[root_b, n] = FPI(1, 1e-8, g)
[root_c, n] = FPI(1, 1e-8, h)