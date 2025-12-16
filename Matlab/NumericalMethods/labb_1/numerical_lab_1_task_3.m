clear

% Summing Riemann zeta

S = zeta(3);

% Summing from n = 1 to n = 10^7
sum1 = 0;
for n = 1:10^7
    sum1 = sum1 + 1/n^3;
end

% Computing error
abs_error_1 = abs(S-sum1)
rel_error_1 = abs(S-sum1)/abs(S)

% abs_error of magnitude 10^-12
% rel_error of magnitude 10^-12

% Summing from n = 10^7 to n = 1
sum2 = 0;
for n = 10^7:-1:1
    sum2 = sum2 + 1/n^3;
end

% Computing error
abs_error_2 = abs(S-sum2)
rel_error_2 = abs(S-sum2)/abs(S)

% abs_error of magnitude 10^-15
% rel_error of magnitude 10^-15

% Computing using vector
vector = zeros(10^7,1);
for n = 1:10^7
    vector(n) = 1/n^3;
end
sum3 = sum(vector);

% Computing error
abs_error_3 = abs(S-sum3)
rel_error_3 = abs(S-sum3)/abs(S)

% abs_error of magnitude 10^-15
% rel_error of magnitude 10^-15

%{
    Summing the series from N to 1 results in better accuracy since the
    small numbers have time to become larger before they are added to the
    larger numbers, thus resulting in smallar rounding errors from
    absorption.

    I would guess MATLABS sum-function does one summation of all elements
    in the vector before rounding, although that doesn't explain the larger
    errors.
%}