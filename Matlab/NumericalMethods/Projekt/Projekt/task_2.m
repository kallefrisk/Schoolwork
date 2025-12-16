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

% Set varable
s = 0.3;
tot_len = adapquad(arcfunc, 0, 1, 1e-6);

% s * arclength(0, 1) - arclength(0, t*(s)) = 0
arc_s = @(t) s*tot_len - adapquad(arcfunc, 0, t, 1e-6);

% Compute t*(s) with interval [0, 1] using bisection method
ts = bisection(0, 1, 1e-4, arc_s);

% Verify result
verification = adapquad(arcfunc, 0, ts, 1e-6)/tot_len;
