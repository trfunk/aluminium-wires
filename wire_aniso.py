import numpy as np
import math
from ansys.mapdl import core as pymapdl
import matplotlib.pyplot as plt

mapdl = pymapdl.launch_mapdl(
    jobname="vsweep_aniso", run_location=r"C:\Users\Tristan\Nextcloud Uni\masterarbeit\tfunk_apdl\sweep_meshed\results")

mapdl.units("SI")
mapdl.prep7()

# Turns out you can create b-splines longer than the 6 allowed via the bsplin() command, by picking up to 18 (?) point via the GUI tool and combining them via P51X


def longer_bspline(keypoints):
    # We pick for the 3rd command field (name including), so we have to pass P51X to the 2nd argument in bsplin()
    mapdl.flst(3, len(keypoints), 3)
    # We graphically pick all the keypoints in the list
    for keypoint in keypoints:
        mapdl.fitem(3, keypoint)
    # All the keypoints get combined in a b(eautiful)-spline, P51X is the graphical selection
    return mapdl.bsplin(p2="P51X")

# create circle
circle = mapdl.cyl4(0, 0, 0.5)

# create path
k1 = mapdl.k("", 0, 0, 0)
k2 = mapdl.k("", 0, 0, 4)
k3 = mapdl.k("", 1, 0, 5)
k4 = mapdl.k("", 3, 0, 6)
k5 = mapdl.k("", 4, 0, 7)
k6 = mapdl.k("", 4, 0, 12)
k7 = mapdl.k("", 3, 0, 13)
k8 = mapdl.k("", 1, 0, 14)
k9 = mapdl.k("", 0, 0, 15)
k10 = mapdl.k("", 0, 0, 19)

kps = [k1, k2, k3, k4, k5, k6, k7, k8, k9, k10]

path = longer_bspline(kps)

# drag circle along path to create wire
wire = mapdl.vdrag(circle, nlp1=path)

# element + mesh for wire
mapdl.et(1, "SOLID186")
element_size = 0.20
mapdl.esize(element_size)
mapdl.vsweep(1, 1, 6)


# working plane for toolhead
mapdl.wplane(wn="1", xorig=0.3501, yorig=-1, zorig=1, xxax=1, yxax=-1, zxax=1, xplan=0.3501,
             yplan=1, zplan=1)  # this has the index 4 and won't clash with the coordinate systems later
mapdl.csys("4")

# toolhead geom
tool_height = 0.2
# width and height are swapped because of the coordinate system
square = mapdl.blc4(xcorner=0, ycorner=0, width=0.5, height=2)
# triangle
tool_k0 = mapdl.k("", 0, 0.5, 0)
tool_k1 = mapdl.k("", tool_height, 0.85, 0)
tool_k2 = mapdl.k("", tool_height, 1.15, 0)
tool_k3 = mapdl.k("", 0, 1.5, 0)
tool = mapdl.a(tool_k0, tool_k1, tool_k2, tool_k3)
tool_slice = mapdl.asba(square, tool)
tool = mapdl.vext(na1=tool_slice, dz=2)

# back to original coordinate system
mapdl.csys("0")
mapdl.wpcsys(wn=1, kcn=0)

# tool mesh + material
mapdl.esize(0.25)
mapdl.et(2, "SOLID187")
mapdl.type(2)
mapdl.vmesh(2)

# contact element bottom, element + material id/secnum/type
mapdl.n(1000001, -0.8, -2, -2)
mapdl.n(1000002, -0.8, -2, 6)
mapdl.n(1000003, -0.8, 2, 6)
mapdl.n(1000004, -0.8, 2, -2)
mapdl.et(3, "TARGE170")
mapdl.type(3)
mapdl.secnum(4)
mapdl.real(0)
mapdl.mat(0)
mapdl.tshap("QUAD")
# Order is important, normal has to face the wire
mapdl.e(1000004, 1000003, 1000002, 1000001)
mapdl.eplot()


mapdl.prep7()
#This can't have a space or anything in its name or path
mapdl.upgeom(fname=r"C:\Users\Tristan\Documents\results\vsweep_fixed", ext="rst", upesys=1)

mapdl.tb("HILL", 1)
mapdl.tbdata(1 , 1.2, 1.2, 1, 1.0, 1.0, 1)


# constraining the bond interface
mapdl.nsel("S", "loc", "z", -2, 3.5)
mapdl.d("ALL", "ALL", 0)
mapdl.allsel()



# constrain thend areas of the wire in UZ direction
mapdl.nsel("S", "loc", "z", 18, 19)
mapdl.d("ALL", "UY", -0.6) 


mapdl.allsel()
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
mapdl.esel("S", "ENAME", vmin=186)
mapdl.triad("LBOT")
mapdl.open_gui()
