function Iapprox=Riemann(funk,a,b,tol)
% Computes Riemann sums for the exponential function

n=1;                        % Antal delintervall/number of subintervals

unclear=true;

while unclear
    
    dx=(b-a)/n;                 % width of subinterval
    P=linspace(a,b,n+1);        % Partition P=[x_0 x_1 x_2 ... x_n]
    
    % Evaluation of function e^x
    fleft=funk(P(1:end-1));      % e^x in points x_{i-1}
    fright=funk(P(2:end));       % e^x in points x_i
    
    % Riemann sums (assumes increasing or decreasing function)
    Rleft=sum(fleft)*dx;        % L if increasing function, U if decreasing         
    Rright=sum(fright)*dx;      % U if increasing function, L if decreasing
    
    L=min(Rleft,Rright);        % Lower Riemann sum
    U=max(Rleft,Rright);        % Upper Riemann sum
    


    if (U-L)<tol
        
        unclear=false;
    
    else
        n=2*n;
    end
end

Iapprox=(U+L)/2;

end

