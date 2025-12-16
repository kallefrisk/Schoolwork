clear
clf


% Set function P
x = @(t) 0.5 + 0.3*t + 3.9*t.^2 - 4.7*t.^3;
y = @(t) 1.5 + 0.3*t + 0.9*t.^2 - 2.7*t.^3;

% Set the derivatives of P
dx = @(t) 0.3 + 7.8*t - 4.7*3*t.^2;
dy = @(t) 0.3 + 1.8*t - 2.7*3*t.^2;

% Set integration limits
t0 = 0;
t1 = 0.5;

% Declare function to integrate arclength
arcfunc = @(t) sqrt(dx(t).^2 + dy(t).^2);

% Compute arclength
length = adapquad(arcfunc, t0, t1, 1e-6);

% Set varable
s = 0.3;
tot_len = adapquad(arcfunc, 0, 1, 1e-6);

% s * arclength(0, 1) - arclength(0, t*(s)) = 0
arc_s = @(t) s*tot_len - adapquad(arcfunc, 0, t, 1e-6);

% Compute t*(s) with interval [0, 1] using bisection method
ts = bisection(0, 1, 1e-4, arc_s);

% Verify result
verification = adapquad(arcfunc, 0, ts, 1e-6)/tot_len;



% Number of equipartitioned segments
n = 20;

% Derivative of arc_s to find t*
darc_s = @(t) (-1) * sqrt(dx(t).^2 + dy(t).^2);

% Create vector to contain all t*-values
t_span_2 = zeros(n+1, 1);

% Record computation speed
tic;

% Compute t*-values
for i = 1:n-1

    % Initial Guess
    init_guess = 1 - 1/i;

    % Compute arc_length
    s = i/n;
    
    % Redefine function with new s_value
    arc_s = @(t) s*tot_len - adapquad(arcfunc, 0, t, 1e-6);

    % Compute t*
    t_span_2(i+1) = newton(init_guess, 1e-4, arc_s, darc_s);
end
t_span_2(end) = 1;

time_2 = toc;


% Create a time-vector to plot the figure using the same amount of
% time-steps
time = linspace(0, 1, (size(t_span_2, 1)-1)*10);

% Plot the non-linear speed figure
figure(1)
plot(x(time), y(time), 'b-')
axis equal
title('Nonlinear speed')
hold on
b = plot(x(0), y(0), 'r.', markersize=10);

for k = time
    b.XData = x(k);
    b.YData = y(k);
    drawnow
    pause(0.01)
end
hold off

% Plot the linearized speed figure
figure(2)
plot(x(time), y(time), 'b-')
axis equal
title('Linearized speed')
hold on
c = plot(x(0), y(0), 'r.', markersize=10);

for k = 1:size(t_span_2, 1) - 1

    % Create sub-set of t from t*n to t*n+1
    time = linspace(t_span_2(k), t_span_2(k+1), 10);

    for j = time
        c.XData = x(j);
        c.YData = y(j);
        drawnow
        pause(0.01)
    end
end
hold off