# Import the necessary modules
from ansys.dpf import post
result_file = r"C:\Users\Tristan\Nextcloud Uni\masterarbeit\tfunk_apdl\axial_compression\results\axial_compression.rst"
simulation = post.StaticMechanicalSimulation(result_file)
print(simulation)

displacement = simulation.displacement(all_sets=True)
force = simulation.element_nodal_forces()
z_displacement = displacement.select(components="Z").select(node_ids=[10,100,1000])



print(z_displacement)