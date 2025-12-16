clear

% Particular periodic solution
u_p = @(t) 1/2*(sin(t) - cos(t));

% Poincaré-map
P = @(u0, t0) u_p(t0) * (1 - exp(-2*pi)) + exp(-2*pi) * u0;

% Define time
time = 0:pi/50:4*pi;
initial = [-1, 0, 1];

% Initialize figure
figure(1)

% Plot periodic solution
plot(time, u_p(time), 'k--', LineWidth=2, DisplayName='Periodic Solution')
hold on

% Plot different initial solutions
for u0 = initial
    [t,u] = ode45(f, time, u0);
    plot(t, u, DisplayName=['u0 = ', num2str(u0)])
end
legend()
hold off

% number of poincaré iterations
n = 10;

% Initial time t0
t0 = 0;
% Initial value u(t0)
u0 = 2;

line = linspace(-1, 3, 1000);

figure(2)
plot(line, line, '-r', LineWidth=1)
hold on
plot(line, P(line, t0), '-b', LineWidth=1.5)
plot(u_p(t0), u_p(t0), 'or')
plot(u0, u0, 'ob')


u = u0;
for i = 1:n
    last = u;
    u = P(last, t0);
    plot([last, last], [last, u], '-g');
    plot([last, u], [u, u], '-g');
end
legend(['Identity Line'], ['P(u)'], ['Fixed Point'], ['Initial Condition'])
hold off



