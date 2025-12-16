clear


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