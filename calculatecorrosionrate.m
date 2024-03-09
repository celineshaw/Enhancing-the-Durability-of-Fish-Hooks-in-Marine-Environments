% Convert resistances from kOhm to Ohm
resistances_ohm = [3.607, 3.52, 3.34, 3.35, 3.378] * 1e3; % Resistances in ohms
areas_cm2 = [7.59625, 14.21940, 10.48765, 15.03785, 17.92228]; % Surface areas in cm^2
B = 0.0317; % Stern-Geary constant in volts (V)

% Constants for copper
K_copper = 3.27e6; % mm g/(A·year) for copper
density_copper = 8.96; % g/cm³ for copper

% Calculate the corrosion current density (i_corr) and corrosion rates (CR)
i_corr_A_cm2 = B ./ resistances_ohm; % Corrosion current density (A/cm²)
CR_mm_year = (K_copper .* i_corr_A_cm2) / density_copper; % Corrosion rate (mm/year)

% Display the results
for i = 1:length(areas_cm2)
    fprintf('Sample %c:\n', 'A' + i - 1);
    fprintf('  Polarization Resistance (R_p): %.2f Ohm\n', resistances_ohm(i));
    fprintf('  Corrosion Current Density (i_corr): %.2e A/cm²\n', i_corr_A_cm2(i));
    fprintf('  Corrosion Rate (CR): %.2f mm/year\n\n', CR_mm_year(i));
end