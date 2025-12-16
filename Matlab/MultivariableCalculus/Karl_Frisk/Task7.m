%% Task7

figure(1)
clf
hold on
grid on
x = -2:0.1:2;
y = -2:0.1:2;
[X,Y] = meshgrid(x,y);
Z = -X-Y;
Z2 = -X-Y+5;
surf(X,Y,Z)
surf(X,Y,Z2)
view(35,35)
hold off
grid off

clear
