%% Task8

[x, y, z] = sphere;

r = 6;

X = x*r;
Y = y*r;
Z = z*r;

figure(1);

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

figure(2);

surf(x, y, z)
title('Sphere using parametrized functions')
axis equal

clear
