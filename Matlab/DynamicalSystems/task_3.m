clear

% Set parameters
a = 5;
h = 0.8;

% number of poincaré iterations
n = 10;

% Initial time t0
t0 = 0;
% Initial value u(t0)
u0 = 0;

% differential equation
f = @(t, u) a*u.*(1-u) - h*(1 + sin(2*pi*t));

% Set integration bounds over one period
time = [t0 t0+1];
% Set ode45 options
options = odeset('RelTol',1e-6,'AbsTol',1e-8);

% Poincaré-map
y = zeros(n+1,1);
y(1) = u0;
for i = 1:n
    [t, u] = ode45(f, time, y(i), options);
    y(i+1) = u(end);
end

line = linspace(min(y)-1, max(y)+1, 1000);
approximation = zeros(size(line));

% Approximate the Poincaré map
for i = 1:size(line, 2)
    [t, u] = ode45(f, time, line(i), options);
    approximation(i) = u(end);
end

% Plot the figure
figure(1)
plot(line, line, '-r')
hold on
plot(line, approximation, '-b')

% Plot the cobweb
u = u0;
for i = 1:n
    plot([y(i), y(i)], [y(i), y(i+1)], '-g')
    plot([y(i), y(i+1)], [y(i+1), y(i+1)], '-g')
end
%axis([-1 1 -5 5])
hold off
