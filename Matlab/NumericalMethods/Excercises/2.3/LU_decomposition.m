function [L,U] = LU_decomposition(A)
%LU_decomposition Factorizes the matrix A into the lower and upper
%triangular matrixes L and U such that L*U=A.
    % Returns [Lower_triangular,Upper_triangular]

B = eye(size(A));

for j = 1:size(A, 2) - 1
    for i = j + 1:size(A, 1)
        if A(j,j) ~= 0
            B(i,j) = A(i,j)/A(j,j);
            A(i,:) = A(i,:) - A(j,:)/A(j,j)*A(i,j);
        else
            break
        end
    end
end

L = B;
U = A;
end

