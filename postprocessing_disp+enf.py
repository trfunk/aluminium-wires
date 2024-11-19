import ansys.dpf.core as dpf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

result_file = r"C:\Users\Tristan\Nextcloud Uni\masterarbeit\tfunk_apdl\transversal_compression\results\transversal_compression.rst"
output_file = r'./tfunk_apdl/transversal_compression/data/displacement_force_data.txt'
scaled_output_file = r'./tfunk_apdl/transversal_compression/data/scaled_displacement_force_data.txt'
output_plot=r'./tfunk_apdl/transversal_compression/force_vs_displacement.pdf'

scaling_factor_displacement = 1
scaling_factor_force = 2


model = dpf.Model(result_file)

# get the displacement and force results
displacement = model.results.displacement
element_nodal_forces = model.results.element_nodal_forces

# get the time frequency support
time_freq_support = model.metadata.time_freq_support

# get the time values
time_values = time_freq_support.time_frequencies.data

# get the number of sets
n_sets = len(time_values)

print(f"Total number of sets: {n_sets}")

# lists to store results
max_displacements = []
force_magnitudes = []

# iterate through each set
for set_index, time_value in enumerate(time_values, 1):
    # create a time scoping for this specific set
    time_scoping = dpf.Scoping()
    time_scoping.location = "time"
    time_scoping.ids = [set_index]

    # evaluate displacement for this set
    disp_field = displacement.on_time_scoping(time_scoping).eval()
    disp_data = disp_field[0].data[:10000] # only consider Cylinder
    disp_x = disp_data[:, 0]  # only consider X component (0 -> X, 1 -> Y, 2 -> Z)
    max_disp = np.max(np.abs(disp_x)) * scaling_factor_displacement  # use absolute value for X component
    max_displacements.append(max_disp)

    # evaluate force for this set
    force_field = element_nodal_forces.on_time_scoping(time_scoping).eval()
    force_data = force_field[0].data[:10000]
    total_force = np.sum(force_data, axis=0) * scaling_factor_force
    force_mag = np.linalg.norm(total_force)
    force_magnitudes.append(force_mag)

    print(f"Set {set_index}: Time = {time_value:.4f}, Max X Displacement = {max_disp:.4f}, Total Force Magnitude = {force_mag:.4f}")

# convert lists to numpy arrays
max_displacements_array = np.array(max_displacements)
force_magnitudes_array = np.array(force_magnitudes)

# find index where Force_Magnitude is first above 0, go back once. Make sure we don't step to -1.
start_index = np.where(force_magnitudes_array > 0)[0][0] - 1
start_index = max(0, start_index)

# scale Max_X_Displacement
scaled_displacement = max_displacements_array[:-start_index]

# trim Force_Magnitude accordingly
scaled_force = force_magnitudes_array[start_index:]

# combine the data and save to files 
combined_data = np.column_stack((max_displacements_array, force_magnitudes_array))
np.savetxt(output_file, combined_data, delimiter=',', header='Max_X_Displacement,Force_Magnitude', comments='')
combined_scaled_data = np.column_stack((scaled_displacement, scaled_force))
np.savetxt(scaled_output_file, combined_scaled_data, delimiter=',', header='Scaled_X_Displacement,Scaled_Force', comments='')
print(f"Data has been saved to {output_file} and {scaled_output_file}")

# create the plot
plt.figure(figsize=(12, 8))

# plot displacement vs force using Seaborn
sns.lineplot(x=max_displacements_array, y=force_magnitudes_array, estimator=None)
sns.lineplot(x=scaled_displacement, y=scaled_force, estimator=None)

# Customize the plot
plt.xlabel('Maximale X-Verschiebung (mm)')
plt.ylabel('Kraft (N)')
plt.title('Kraft-Verschiebungskurve (Zylinder)')

# show the plot
plt.savefig(output_plot, format='pdf', dpi=300)
plt.show()
