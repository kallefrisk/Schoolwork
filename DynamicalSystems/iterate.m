function y=iterate(fcn,x0,n)
y = zeros(n+1, 1);
y(1)=fcn(x0);
for i=1:n
    y(i+1)=fcn(y(i));
end
y=y';
end