% Polarization resistance values for each fish hook in kOhms
Rp_values_kOhm = [3.607, 3.52, 3.34, 3.35, 3.378];

% Convert kOhms to Ohms
Rp_values_Ohm = Rp_values_kOhm * 1e3; % Ohms

% Surface areas for each fish hook in cm^2
areas_cm2 = [7.59625, 14.21940, 10.48765, 15.03785, 17.92228];

% Assume a hypothetical voltage applied across each fish hook (in volts)
V_applied = 0.0317; % Example voltage

% Calculate current (I) using Ohm's Law: I = V / R for each fish hook
currents_A = V_applied ./ Rp_values_Ohm; % Current in Amperes (A)

% Calculate current density (J) for each fish hook: J = I / A
current_densities_A_cm2 = currents_A ./ areas_cm2; % Current density in A/cm^2

% Plot current density for each fish hook using filled markers
labels = {'A', 'B', 'C', 'D', 'E'};
figure;
scatter(1:length(areas_cm2), current_densities_A_cm2, 'filled');
set(gca, 'xtick', 1:length(areas_cm2), 'xticklabel', labels);

% Label the plot
title('Current Density for Each Fish Hook');
xlabel('Fish Hook Label');
ylabel('Current Density (A/cm^2)');
grid on;

% Create a table with the data
T = table(labels', Rp_values_kOhm', Rp_values_Ohm', areas_cm2', currents_A', current_densities_A_cm2', ...
    'VariableNames', {'Fish Hook', 'Polarization Resistance (kOhm)', 'Polarization Resistance (Ohm)', ...
    'Surface Area (cm^2)', 'Current (A)', 'Current Density (A/cm^2)'});

% Display the table
disp(T);

% Display the data in a UI table
fig = uifigure('Name', 'Data Table'); % Create a UI figure instead of a regular figure
u = uitable(fig, 'Data', T, 'ColumnName', T.Properties.VariableNames, ...
    'Position', [20 20 fig.Position(3)-40 fig.Position(4)-40]); % Adjust size to the figure