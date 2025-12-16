function [r] = newton(x_0, tol, f, df)
%NEWTON Summary of this function goes here
%   Detailed explanation goes here
x = x_0 - f(x_0)./df(x_0);
while abs((x - f(x)./df(x)) - x)/x > tol
    x = x - f(x)./df(x);
end

r = x;