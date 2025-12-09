%% Task1

t = 1:0.01:5;
x = 4 + t.^3;
y = 1 + 5*t.^2;

figure(1)

plot(x, y)

clear

%% Task2

r = 3;
theta = 0:pi/500:2*pi;
x = r*cos(theta);
y = r*sin(theta);

figure(2)

plot(x, y)

clear

%% Task3

theta = 0:pi/500:2*pi;
r = 1 - sin(4*theta);
x = r.*cos(theta);
y = r.*sin(theta);

plot(x, y)

clear

%% Task4

t = -2*pi:pi/250:2*pi;
x = sin(2*t);
y = cos(2*t);
z = sin(3*t);

figure(4)

plot3(x, y, z)

clear

%% Task5

theta = 0:pi/500:4*pi;
r = 2;
x = r*cos(theta);
y = r*sin(theta);
z = theta/2/pi;

figure(5)

plot3(x, y, z)

clear

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

%% Task7

figure(6)
clf

hold on
grid on

x = -2:0.1:2;
y = -2:0.1:2;
[X,Y] = meshgrid(x,y);
Z = -X-Y;

surf(X,Y,Z)
view(35,35)
hold off
grid off

clear

%% Task8

[x, y, z] = sphere;

r = 6;
X = x*r;
Y = y*r;
Z = z*r;

figure(7)

surf(X-2, Y+1, Z+3)
title('Sphere using "sphere" function')
axis equal

clear

rho = 6;

theta = 0:pi/25:2*pi;
phi = 0:pi/50:pi;

[theta, phi] = meshgrid(theta, phi);

x = rho*sin(phi).*cos(theta) - 2;
y = rho*sin(phi).*sin(theta) + 1;
z = rho*cos(phi) + 3;

figure(8)

surf(x, y, z)
title('Sphere using parametrized functions')
axis equal

clear

%% Task9

x = -5:0.1:5;
y = -5:0.1:5;

[x, y] = meshgrid(x, y);

z1 = 2*x.^2+2*y.^2;
figure(9)
surf(x, y, z1)
contour(x, y, z1, 5)

z2 = sin(x) + cos(5*y);
figure(10)
surf(x, y, z2)
contour(x, y, z2, 5)

z3 = 1./(x.*(2) + y.^(2));
figure(11)
surf(x, y, z3)
contour(x, y, z3, 5)

z4 = sqrt(abs(6 - x.^(2) - y.^(2)));
figure(12)
surf(x, y, z4)
contour(x, y, z4, 5)

clear

%% Task10

f = @(x) 1./(1 + x).^2;

I_value = integral(f, 0, 1)

clear

