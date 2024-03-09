% Define the filenames
filenames = {'A.xy', 'B.xy', 'C.xy', 'D.xy', 'E.xy'};

% Predefine colors for the plots
colors = lines(numel(filenames));

% Create a new figure
figure;

% Loop over each file
for i = 1:length(filenames)
    % Read the data from the file
    data = dlmread(filenames{i});
    
    % Extract the angle (2-theta) and intensity columns
    two_theta = data(:, 1);
    intensity = data(:, 2);
    
    % Plot the data
    plot(two_theta, intensity, 'Color', colors(i, :), 'DisplayName', filenames{i});
    
    % Hold on to the current plot so that the next data series can be added
    hold on;
end

% Customize the graph
xlabel('2\theta (degrees)');
ylabel('Intensity (arbitrary units)');
title('XRD Patterns');
legend('-DynamicLegend'); % Update the legend dynamically
grid on;
hold off; % Release the plot hold so that new plots do not overlap