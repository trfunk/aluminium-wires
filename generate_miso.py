import numpy as np
import matplotlib.pyplot as plt

# load the data
data = np.loadtxt('./tfunk_apdl/axial_compression/data/MeanCurve.mean')
nominal_strain = data[:, 0]
nominal_stress = data[:, 1]

true_stress = nominal_stress * (1 + nominal_strain)

true_strain = np.log(1 + nominal_strain)

E = nominal_stress[1] / nominal_strain[1] # alternatively use 72000 N/mm^2

elastic_strain = true_stress / E

plastic_strain = true_strain - elastic_strain

# output array
output = np.column_stack((plastic_strain, true_stress))

# save output
np.savetxt('true_stress_plastic_strain.txt', output, fmt='%.4f', header='epsilon_p, sigma_t')

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(plastic_strain, true_stress, 'b-')
plt.xlabel('Plastische Logarithmische Dehnung')
plt.ylabel('Wahre Spannung [MPa]')
plt.legend()
plt.grid(True)
plt.show()
