function [r, n] = bisection(l, u, tol, f)
%BISECTION Summary of this function goes here
%   Detailed explanation goes here
count = 0;
while (u-l)/2 > tol
    new = (l+u)/2;
    count = count + 1;
    if f(l)*f(new) > 0
        l = new;
    else
        u = new;
    end
end

r = (l+u)/2;
n = count + 1;