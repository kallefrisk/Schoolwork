function y=cobweb_copy(x,n)
y = zeros(2*n-1,2);
for i=0:n-2
    y(2*i+1,1)=x(i+1);
    y(2*i+1,2)=x(i+1);
    y(2*i+2,1)=x(i+1);
    y(2*i+2,2)=x(i+2);
end
end

