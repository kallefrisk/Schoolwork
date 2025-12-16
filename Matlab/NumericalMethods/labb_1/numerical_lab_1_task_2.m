clear

% Demonstrating k=48 is the largest integer in Sauer 0.3.4

for k = 46:50
    a = 19 + 2^(-k);
    b = 19;
    res = (a > b) * k
end