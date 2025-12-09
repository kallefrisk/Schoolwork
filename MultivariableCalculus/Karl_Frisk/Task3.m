%% Task3

theta = 0:pi/500:2*pi;
r = 1 - sin(4*theta);
x = r.*cos(theta);
y = r.*sin(theta);

figure(1)
plot(x, y)
axis equal;
figure(2)
polarplot(theta, r)

clear