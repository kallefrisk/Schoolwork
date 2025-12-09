clear
clf
format long

f = @(x) det([1 2 3 x; 4 5 x 6; 7 x 8 9; x 10 11 12]) - 1000;

x = -18:0.1:10;
y = arrayfun(f, x);

plot(x, zeros(length(x)))
hold on
plot(x, y)
hold off

root_1 = bisection(-30, 0, 1e-6, f)
a = f(root_1)
root_2 = bisection(0, 30, 1e-6, f)
b = f(root_2)