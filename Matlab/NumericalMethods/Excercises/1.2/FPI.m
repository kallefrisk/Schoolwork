function [r, n] = FPI(x_0, tol, f)
%FPI Summary of this function goes here
%   Detailed explanation goes here
count = 0;
while abs(f(x_0) - x_0)/x_0 > tol
    x_0 = f(x_0);
    count = count + 1;
    if count > 100
        break
    end
end

r = x_0;
n = count;