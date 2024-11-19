import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
sns.set_context("paper", font_scale = 1)

# i'm sorry for this atrocious script design

# Function to read the data file
def read_displacement_force_data(filename, symmetrical=False, color="blue", style="solid"):
    data = np.loadtxt(filename, delimiter=',', skiprows=1)
    displacement = data[:, 0]
    if symmetrical:
        force = data[:, 1]
    else:
        force = data[:, 1] * 2
    ax = sns.lineplot(x=displacement, y=force, color=color, linestyle=style, errorbar=None, estimator=False)

def read_cut_data(filename, color="blue", style="solid"):
    data = np.loadtxt(filename, delimiter=' ')
    displacement = data[:, 0]
    force = data[:, 1] 
    ax = sns.lineplot(x=displacement, y=force, color=color, linestyle=style, errorbar=None, estimator=False)


plt.figure(figsize=(10, 6))

read_displacement_force_data("./tfunk_apdl/transversal_compression/data/scaled_displacement_force_data.txt", True, "blue", "solid")
read_displacement_force_data("./tfunk_apdl/transversal_compression/data/scaled_displacement_force_data_aniso.txt", True, "blue", "dashed")
read_displacement_force_data("./tfunk_apdl/transversal_compression/data/scaled_displacement_force_data_sym.txt", True, "orange", "solid")
read_displacement_force_data("./tfunk_apdl/transversal_compression/data/scaled_displacement_force_data_sym_aniso.txt", True, "orange", "dashed")
read_displacement_force_data("./tfunk_apdl/transversal_compression/data/scaled_displacement_force_data_lockedZ.txt", True, "green", "solid")
read_displacement_force_data("./tfunk_apdl/transversal_compression/data/scaled_displacement_force_data_lockedZ_aniso.txt", True, "green", "dashed")

read_cut_data("./tfunk_apdl/transversal_compression/data/D3.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/D8.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/D9.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/E1.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/E2.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/E3.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/E4.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/E6.cut", "red")
read_cut_data("./tfunk_apdl/transversal_compression/data/F2.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/F3.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/F5.cut", "red") 
read_cut_data("./tfunk_apdl/transversal_compression/data/F9.cut", "red") 

plt.xlabel('Verschiebung (mm)')
plt.ylabel('Standardkraft (N)')
leg = plt.legend(["Isotrop", "Anisotrop", "Isotrop mit Länge 0.5 mm", "Anisotrop mit Länge 0.5 mm", "Isotrop Gekoppelte Z", "Anisotrop Gekoppelte Z", "Messdaten"])
leg_lines = leg.get_lines()
print(leg_lines)
plt.savefig(r'./tfunk_apdl/transversal_compression/data/trans_scaled_comparison_force_vs_displacement.pdf', format='pdf', dpi=300, bbox_inches='tight')
plt.show()


    
