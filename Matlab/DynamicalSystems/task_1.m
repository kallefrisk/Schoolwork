clear

global K;

K = 2;
figure(1)
axis([0 K 0 3])

[x,y]=meshgrid(.1:K/20:K,.1:.15:3);
dx=x.*((1-x/K).*(x+1)-y);
dy=y.*(x-1);
quiver(x,y,dx,dy)
hold on;

t=0:.01:K;

plot(t,(1-t/K).*(t+1),'-r')
plot(ones(size(t)),t*3/K,'-g')

options=odeset('AbsTol',1e-6,'RelTol',1e-3,'MaxStep',0.1);

for n = 0:0.5:2.5
    [~,y]=ode45(@syst_exampl,[0 20],[2 n],options);
    plot(y(:,1),y(:,2),'-k')
end
hold off;


syms x y;
dx = x*((1-x/K)*(x+1)-y);
derivative = diff(dx, x);
sign_at_intersect = subs(derivative, x, 1);
sign_at_intersect_1 = subs(sign_at_intersect, y, 1)


K = 5;
figure(2)
axis([0 K 0 3])

[x,y]=meshgrid(.1:K/20:K,.1:.15:3);
dx=x.*((1-x/K).*(x+1)-y);
dy=y.*(x-1);
quiver(x,y,dx,dy)
hold on;

t=0:.01:K;

plot(t,(1-t/K).*(t+1),'-r')
plot(ones(size(t)),t*3/K,'-g')

for n = 0:0.75:2.25
    [~,y]=ode45(@syst_exampl,[0 20],[1 n],options);
    plot(y(:,1),y(:,2),'-k')
end
hold off;


syms x y;
dx = x*((1-x/K)*(x+1)-y);
derivative = diff(dx, x);
sign_at_intersect = subs(derivative, x, 1);
sign_at_intersect_2 = subs(sign_at_intersect, y, 8/5)


figure(3)
K=5;
[~,y]=ode45(@syst_exampl,[0 200],[1 8/5+.01],options);
plot(y(:,1),y(:,2),'-k')
hold on;
[~,y]=ode45(@syst_exampl,[0 200],[5 .01],options);
plot(y(:,1),y(:,2),'-k')
hold off

global c
global k
c=1.8;
k=2;
y=iterate(@tent_v2,0,30);
z=cobweb_copy(y,31);
figure(4)
plot(z(:,1),z(:,2),'-b')
hold on;
t=-1.6:.01:1.3;
plot(t,t,'-r')
plot(t,tent_v2(t),'-y')
hold off;
