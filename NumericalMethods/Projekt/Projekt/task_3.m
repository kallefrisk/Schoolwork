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
n = 10;

% Create vector to contain all t*-values
t_span_1 = zeros(n+1, 1);

% Record computation speed
tic;

% Compute t*-values
for i = 1:n-1

    % Compute arc_length
    s = i/n;
    
    % Redefine function with new s_value
    arc_s = @(t) s*tot_len - adapquad(arcfunc, 0, t, 1e-6);

    % Compute t*
    t_span_1(i+1) = bisection(0, 1, 1e-4, arc_s);
end
t_span_1(end) = 1;

time_1 = toc;

% Plot results
figure(1)
hold on

% Iterate over found t*
for k = 1:size(t_span_1, 1) - 1

    % Create sub-set of t from t*n to t*n+1
    time = linspace(t_span_1(k), t_span_1(k+1), 10);

    % Plot the sections and the separation-points
    plot(x(time), y(time))
    plot(x(t_span_1(k)), y(t_span_1(k)), 'kx')
end
plot(x(t_span_1(end)), y(t_span_1(end)), 'kx')

% Axis equal to properly see that the sections are equal in length
axis equal
title([num2str(n), ' Segments using Bisection Method in ', num2str(time_1), ' seconds!'])
xlabel('x')
ylabel('y')
hold off
