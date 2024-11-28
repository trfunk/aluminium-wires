import numpy as np
import math
from ansys.mapdl import core as pymapdl
import matplotlib.pyplot as plt

mapdl = pymapdl.launch_mapdl(jobname="axial_compression",
                             run_location=r"C:\Users\Tristan\Nextcloud Uni\masterarbeit\tfunk_apdl\axial_compression\results")

mapdl.units("uMKS")
mapdl.prep7()

# Define the base area of the cylinder and extrude it by dz
circle = mapdl.cyl4(0, 0, rad1=0.5)
cylinder = mapdl.vext(circle, dz=0.5)
mapdl.et(1, "SOLID187")
mapdl.esize(0.1)
mapdl.vmesh(1)

# material
mapdl.mp("EX", 1, 70000)
mapdl.mp("NUXY", 1, 0.33)
mapdl.tb("PLASTIC", 1, 0, 100, "MISO")
mapdl.tbtemp(0)
mapdl.tbpt("DEFI", 0., 35)
mapdl.tbpt("DEFI", 0.01, 39.93)
mapdl.tbpt("DEFI", 0.02, 43.32)
mapdl.tbpt("DEFI", 0.03, 45.77)
mapdl.tbpt("DEFI", 0.04, 47.65)
mapdl.tbpt("DEFI", 0.05, 49.18)
mapdl.tbpt("DEFI", 0.06, 50.5)
mapdl.tbpt("DEFI", 0.07, 51.7)
mapdl.tbpt("DEFI", 0.08, 52.82)
mapdl.tbpt("DEFI", 0.09, 53.89)
mapdl.tbpt("DEFI", 0.1, 54.93)
mapdl.tbpt("DEFI", 0.11, 55.96)
mapdl.tbpt("DEFI", 0.12, 56.98)
mapdl.tbpt("DEFI", 0.13, 57.98)
mapdl.tbpt("DEFI", 0.14, 58.99)
mapdl.tbpt("DEFI", 0.15, 59.99)
mapdl.tbpt("DEFI", 0.16, 61)
mapdl.tbpt("DEFI", 0.17, 62)
mapdl.tbpt("DEFI", 0.18, 63)
mapdl.tbpt("DEFI", 0.19, 64)
mapdl.tbpt("DEFI", 0.2, 65)
mapdl.tbpt("DEFI", 0.21, 66)
mapdl.tbpt("DEFI", 0.22, 67)
mapdl.tbpt("DEFI", 0.23, 68)
mapdl.tbpt("DEFI", 0.24, 69)
mapdl.tbpt("DEFI", 0.25, 70)
mapdl.tbpt("DEFI", 0.26, 71)
mapdl.tbpt("DEFI", 0.27, 72)
mapdl.tbpt("DEFI", 0.28, 73)
mapdl.tbpt("DEFI", 0.29, 74)
mapdl.tbpt("DEFI", 0.3, 75)
mapdl.tbpt("DEFI", 0.31, 76)
mapdl.tbpt("DEFI", 0.32, 77)
mapdl.tbpt("DEFI", 0.33, 78)
mapdl.tbpt("DEFI", 0.34, 79)
mapdl.tbpt("DEFI", 0.35, 80)
mapdl.tbpt("DEFI", 0.36, 81)
mapdl.tbpt("DEFI", 0.37, 82)
mapdl.tbpt("DEFI", 0.38, 83)
mapdl.tbpt("DEFI", 0.39, 84)
mapdl.tbpt("DEFI", 0.4, 85)
mapdl.tbpt("DEFI", 0.41, 86)
mapdl.tbpt("DEFI", 0.42, 87)
mapdl.tbpt("DEFI", 0.43, 88)
mapdl.tbpt("DEFI", 0.44, 89)
mapdl.tbpt("DEFI", 0.45, 90)
mapdl.tbpt("DEFI", 0.46, 91)
mapdl.tbpt("DEFI", 0.47, 92)
mapdl.tbpt("DEFI", 0.48, 93)
mapdl.tbpt("DEFI", 0.49, 94)
mapdl.tbpt("DEFI", 0.5, 95)
mapdl.tbpt("DEFI", 0.51, 96)
mapdl.tbpt("DEFI", 0.52, 97)
mapdl.tbpt("DEFI", 0.53, 98)
mapdl.tbpt("DEFI", 0.54, 99)
mapdl.tbpt("DEFI", 0.55, 100)
mapdl.tbpt("DEFI", 0.56, 101)
mapdl.tbpt("DEFI", 0.57, 102)
mapdl.tbpt("DEFI", 0.58, 103)
mapdl.tbpt("DEFI", 0.59, 104)
mapdl.tbpt("DEFI", 0.6, 105)
mapdl.tbpt("DEFI", 0.61, 106)
mapdl.tbpt("DEFI", 0.62, 107)
mapdl.tbpt("DEFI", 0.63, 108)
mapdl.tbpt("DEFI", 0.64, 109)
mapdl.tbpt("DEFI", 0.65, 110)
mapdl.tbpt("DEFI", 0.66, 111)
mapdl.tbpt("DEFI", 0.67, 112)
mapdl.tbpt("DEFI", 0.68, 113)
mapdl.tbpt("DEFI", 0.69, 114)
mapdl.tbpt("DEFI", 0.7, 115)
mapdl.tbpt("DEFI", 0.71, 116)
mapdl.tbpt("DEFI", 0.72, 117)
mapdl.tbpt("DEFI", 0.73, 118)
mapdl.tbpt("DEFI", 0.74, 119)
mapdl.tbpt("DEFI", 0.75, 120)
mapdl.tbpt("DEFI", 0.76, 121)
mapdl.tbpt("DEFI", 0.77, 122)
mapdl.tbpt("DEFI", 0.78, 123)
mapdl.tbpt("DEFI", 0.79, 124)
mapdl.tbpt("DEFI", 0.8, 125)
mapdl.tbpt("DEFI", 0.81, 126)
mapdl.tbpt("DEFI", 0.82, 127)
mapdl.tbpt("DEFI", 0.83, 128)
mapdl.tbpt("DEFI", 0.84, 129)
mapdl.tbpt("DEFI", 0.85, 130)
mapdl.tbpt("DEFI", 0.86, 131)
mapdl.tbpt("DEFI", 0.87, 132)
mapdl.tbpt("DEFI", 0.88, 133)
mapdl.tbpt("DEFI", 0.89, 134)
mapdl.tbpt("DEFI", 0.9, 135)
mapdl.tbpt("DEFI", 0.91, 136)
mapdl.tbpt("DEFI", 0.92, 137)
mapdl.tbpt("DEFI", 0.93, 138)
mapdl.tbpt("DEFI", 0.94, 139)
mapdl.tbpt("DEFI", 0.95, 140)
mapdl.tbpt("DEFI", 0.96, 141)
mapdl.tbpt("DEFI", 0.97, 142)
mapdl.tbpt("DEFI", 0.98, 143)
mapdl.tbpt("DEFI", 0.99, 144)


# uncomment for anisotropic behaviour
#mapdl.tb("HILL", 1)
#mapdl.tbdata(1, 0.7, 0.7, 1.0, 0.8, 0.8, 0.6)

# target plate
mapdl.real(1)
mapdl.n(100001, -1, -1, 0.5001)
mapdl.n(100002, 1, -1, 0.5001)
mapdl.n(100003, 1, 1, 0.5001)
mapdl.n(100004, -1, 1, 0.5001)
mapdl.et(2, 170)
mapdl.type(2)
mapdl.tshap("QUAD")

# Order is important, normal has to face cylinder. Doing 100001 -> 1000004 causes the normal to point away from the cylinder, causing penetration
target = mapdl.e(100004, 100003, 100002, 100001)

# contact on A2 - A6
mapdl.et(3, 174)
mapdl.type(3)
mapdl.asel("S", "AREA", vmin=2, vmax=6, vinc=1)
mapdl.nsla("S", 1)
mapdl.esurf()
mapdl.allsel()

# constraints cylinder
mapdl.asel("S", vmin=1)
mapdl.nsla("S", 1)
mapdl.dsym("SYMM", "Z")
mapdl.d("ALL", "UX", 0)
mapdl.d("ALL", "UY", 0)
mapdl.allsel()
#mapdl.d(88, "UX", 0)
#mapdl.d(88, "UY", 0)
#mapdl.d(55, "UY", 0)

# constraints target
mapdl.nsel("S", "NODE", vmin=100001, vmax=100004)
mapdl.d("ALL", "UX", 0)
mapdl.d("ALL", "UY", 0)
mapdl.d("ALL", "UZ", -0.3001)  # 0.1 gap
mapdl.allsel()

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
