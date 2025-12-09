% Define the number of terms in the Fourier series
N = 50;

% Define the range of t values
t_values = linspace(-pi, pi, 1000);

% Initialize the Fourier series sum
fourier_series = zeros(size(t_values));

% Compute the Fourier series
for n = 1:N
    % Fourier coefficients for the given function
    a0 = pi / 2; % DC component
    an = (2/(pi*n^2)) * ((-1)^n - 1); % Cosine coefficients
    bn = (-1)^(n+1) / n; % Sine coefficients

    % Add the nth term to the Fourier series
    fourier_series = fourier_series + an * cos(n*t_values) + bn * sin(n*t_values);
end

% Add the DC component
fourier_series = fourier_series + a0 / 2;

% Plot the original function and the Fourier series approximation
figure;
hold on;
plot(t_values, fourier_series, 'LineWidth', 2, 'DisplayName', 'Fourier Series');

% Plot the original piecewise function
original_function = @(t) (t >= 0 & t < pi) .* t;
plot(t_values, original_function(t_values), 'LineWidth', 2, 'DisplayName', 'Original Function');

% Add labels and legend
xlabel('t');
ylabel('f(t)');
title('Fourier Series Approximation');
legend show;
grid on;
hold off;