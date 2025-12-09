%% Task6

A = [1, 0, 3; 0, 4, 5;1, 2, -1];
B = [1, 3, 1; 2, 2, 2; 3, 1, 3];
a = [2; 3; 0];
b = [1; 1; 1];

c1 = A*B
c2 = A*a
% c3 = B*b.'
% c4 = a*A
c5 = b.'*B
c6 = a.'*b
c7 = a*b.'
c8 = a.*b
c9 = A.*B

clear
% c3 and c4 does not compute since the matrix dimensions do not align with the given rules for matrix multiplication.
