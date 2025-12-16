function xdot=syst_exampl(~,x)
global K
xdot=[x(1).*((1-x(1)/K).*(x(1)+1)-x(2));x(2).*(x(1)-1)];
end
