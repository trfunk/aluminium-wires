import numpy as np
from ansys.mapdl import core as pymapdl
import matplotlib.pyplot as plt

mapdl = pymapdl.launch_mapdl(jobname="transversal_compression",
                             run_location=r"C:\Users\Tristan\Nextcloud Uni\masterarbeit\tfunk_apdl\transversal_compression\results")

mapdl.units("SI")
mapdl.prep7()

# geom + mesh
circle = mapdl.cyl4(0, 0, rad1=0.5, theta1=0, theta2=90)
cylinder = mapdl.vext(circle, dz=1)
mapdl.et(1, "SOLID187")
mapdl.esize(0.1)
mapdl.vmesh(1)

# material
mapdl.mp("EX", 1, 70000)
mapdl.mp("NUXY", 1, 0.33)
mapdl.tb("PLASTIC", 1, 0, 100, "MISO")
mapdl.tbtemp(0)
mapdl.tbpt("DEFI", 0.00, 35)
# omitted, see github
mapdl.tbpt("DEFI", 0.99, 144)
#mapdl.tb("hill", 1)
#mapdl.tbdata(1.2, 1.2, 1.0, 0.9, 0.9, 0.80, 0.80)

# target plate
mapdl.real(1)
mapdl.n(100001, 0.51, -0.75, -0.75)
mapdl.n(100002, 0.51, -0.75, 3)
mapdl.n(100003, 0.51, 2, 3)
mapdl.n(100004, 0.51, 2, -0.75)
mapdl.et(2, 170)
mapdl.type(2)
mapdl.tshap("QUAD")
mapdl.e(100001, 100002, 100003, 100004)

# contact on A3 + A5
mapdl.et(3, 174)
mapdl.type(3)
mapdl.asel("S", "AREA", vmin=3, vmax=5, vinc=2)
mapdl.nsla("S", 1)
mapdl.esurf()
mapdl.allsel()

# constraints cylinder
mapdl.asel("S", "AREA", vmin=4)
mapdl.nsla("S", 1)
mapdl.dsym("SYMM", "X")
mapdl.allsel()
mapdl.asel("S", "AREA", vmin=5)
mapdl.nsla("S", 1)
mapdl.dsym("SYMM", "Y")
#mapdl.d(553, "UZ", 0)
mapdl.allsel()
mapdl.da(1,"UZ", 0)
# constraints target
mapdl.nsel("S", "NODE", vmin=100001, vmax=100004)
mapdl.d("ALL", "UZ", 0)
mapdl.d("ALL", "UY", 0)
mapdl.d("ALL", "UX", -0.41)
mapdl.allsel()

# uncommment this to couple the Z-coordinates of all nodes in area 2 
#mapdl.asel("S", "AREA", vmin=2)
#mapdl.nsla("S", 1)

#mapdl.cm('AREA_NODES', 'NODE')
#mapdl.cp('NEXT', 'UZ', 'AREA_NODES')
#mapdl.allsel()
#mapdl.cplist('ALL')

# keyopts
mapdl.keyopt("CONT", 7, 1)

# finish
mapdl.finish()
mapdl.run("/SOLU")
mapdl.antype("static")

# Activate non-linear geometry
mapdl.nlgeom("on")

# Request substeps
mapdl.autots(key="on")
mapdl.nsubst(nsbstp=100, nsbmx=100, nsbmn=100)
mapdl.kbc(key=0)
mapdl.outres("all", "all")

# Solve
output = mapdl.solve()
print(output)
result = mapdl.result
mapdl.open_gui()
