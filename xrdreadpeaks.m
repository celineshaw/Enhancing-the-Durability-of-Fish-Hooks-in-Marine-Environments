
% Define the folder where you want to save the JPEG files
output_folder = 'C:/Users/celineshaw/Desktop/MSE 140A';  

% Define the filenames
filenames = {'A.xy', 'B.xy', 'C.xy', 'D.xy', 'E.xy'};

% Loop over each file
for i = 1:length(filenames)
    % Read the data from the file
    data = dlmread(filenames{i});
    
    % Extract the angle (2-theta) and intensity columns
    two_theta = data(:, 1);
    intensity = data(:, 2);

    % Detect peaks
    [peaks, locs] = findpeaks(intensity, two_theta, 'MinPeakProminence', 0.1 * max(intensity));

    % Create a figure for each pattern
    figure;
    
    % Plot the original data
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
    title(['XRD Pattern with Detected Peaks for ', filenames{i}]);
    grid on;
    hold off;

    % Save the figure as a JPEG file
    jpg_filename = [filenames{i}, '.jpg'];
    saveas(gcf, jpg_filename, 'jpeg');

    % Close the figure to avoid having too many open windows
    %close(gcf);
    
 
end