%% Task9

% Equation 1

x = -5:0.1:5;
y = -5:0.1:5;

[x, y] = meshgrid(x, y);

z1 = 2*x.^2+2*y.^2;
figure(1)
surf(x, y, z1)
figure(2)
contour(x, y, z1, 5)


clear

% Equation 2

x = 0:pi/25:2*pi;
y = 0:pi/25:2*pi;

[x, y] = meshgrid(x, y);

z2 = sin(x) + cos(5*y);
figure(3)
surf(x, y, z2)
figure(4)
contour(x, y, z2, 5)


clear

% Equation 3

x = -1:0.05:1;
y = -1:0.05:1;

[x, y] = meshgrid(x, y);

z3 = 1./(x.^2 + y.^2);
figure(5)
surf(x, y, z3)
figure(6)
contour(x, y, z3, 5)


clear

% Equation 4

x = -sqrt(6):0.05:sqrt(6);
y = -sqrt(6):0.05:sqrt(6);

[x, y] = meshgrid(x, y);

z4 = sqrt(6 - x.^(2) - y.^(2));

z4(imag(z4) ~= 0) = NaN;

figure(7)
surf(x, y, z4)
title('Plotting only the positive half of the sphere')
axis equal;

[X,Y,Z] = sphere;
figure(8)
surf(X*sqrt(6),Y*sqrt(6),Z*sqrt(6))
title('plotting the entire sphere')
axis equal;

figure(9)
contour(x, y, z4, 5)


clear
