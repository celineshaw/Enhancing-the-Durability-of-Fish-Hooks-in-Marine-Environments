% Read the data (this assumes you have loaded your data into 'two_theta' and 'intensity' arrays)
 data = dlmread('A.xy');
 two_theta = data(:, 1);
 intensity = data(:, 2);

% Detect peaks
[peaks, locs] = findpeaks(intensity, two_theta, 'MinPeakProminence', 0.1 * max(intensity));

% Plot the original data
figure;
plot(two_theta, intensity);
hold on;

% Plot detected peaks
plot(locs, peaks, 'r^', 'MarkerFaceColor', 'r');

% Annotate the peaks
text(locs, peaks, arrayfun(@num2str, locs, 'UniformOutput', false), ...
    'HorizontalAlignment', 'center', 'VerticalAlignment', 'bottom');

% Additional plot formatting
xlabel('2\theta (degrees)');
ylabel('Intensity (arbitrary units)');
title('XRD Pattern with Detected Peaks');
grid on;
hold off;