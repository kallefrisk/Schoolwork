function y=tent_v2(x)
global c;
global k;
[m,n]=size(x);
y = zeros(m,n);
for i=1:m
    for j=1:n
        if x(i,j)<0
            y(i,j)=1+c*x(i,j);
        else
            y(i,j)=1-k*x(i,j);
        end
    end
end

end

