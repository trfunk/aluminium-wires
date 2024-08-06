import numpy as np
import math
from ansys.mapdl import core as pymapdl
import matplotlib.pyplot as plt

# import pyvista
# pymapdl.change_default_ansys_path("/mnt/work/ansys_inc/v241/ansys/bin/ansys241")
# pyvista.start_xvfb()


mapdl = pymapdl.launch_mapdl(jobname="vsweep", run_location=r"C:\Users\Tristan\Nextcloud Uni\masterarbeit\tfunk_apdl\sweep_meshed\results")

mapdl.units("SI")
mapdl.prep7()

# create circle we drag along our path
circle = mapdl.cyl4(0, 0, 0.5)


# Turns out you can create b-splines longer than the 6 allowed via the bsplin() command, by picking up to 18 (?) point via the GUI tool and combining them via P51X
def longer_bspline(keypoints):
    # We pick for the 3rd command field (name including), so we have to pass P51X to the 2nd argument in bsplin()
    mapdl.flst(3, len(keypoints), 3)
    # We graphically pick all the keypoints in the list
    for keypoint in keypoints:
        mapdl.fitem(3, keypoint)
    # All the keypoints get combined in a b(eautiful)-spline, P51X is the graphical selection
    return mapdl.bsplin(p2="P51X")


# Assumptions: Not Negative
def calculate_tilt(element):
    angles = []
    i, j, k, l, m, n, o, p = [
        node for node in element[-20:-12]]  # Grab the first 8 nodes
    angles.append(calculate_angle(i, m))
    angles.append(calculate_angle(j, n))
    angles.append(calculate_angle(k, o))
    angles.append(calculate_angle(l, p))
    # tilt the other way if the element is slanted downwards
    if mapdl.queries.nx(i) > mapdl.queries.nx(m):
        return -1 * np.average(angles)
    return np.average(angles)


# Slope dx/dZ, dZ never 0 because tilt <90°
def calculate_angle(node1, node2):
    i = [mapdl.queries.nx(node1), 0, mapdl.queries.nz(node1)]
    m = [mapdl.queries.nx(node2), 0, mapdl.queries.nz(node2)]
    u = [mapdl.queries.nx(node1), 0, mapdl.queries.nz(node2)]
    im = math.dist(i, m)
    iu = math.dist(i, u)
    angle = math.degrees(math.acos(iu/im))
    return angle


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


# mapdl.lplot(show_bounds=True, show_keypoint_numbering=True)
wire = mapdl.vdrag(circle, nlp1=path)

# Element Type + Mesh size for wire
mapdl.et(1, "SOLID186")
element_size = 0.20
mapdl.esize(element_size)

# https://mapdl.docs.pyansys.com/version/stable/mapdl_commands/prep7/_autosummary/ansys.mapdl.core.Mapdl.vsweep.html
mapdl.vsweep(1, 1, 6)
mapdl.eplot(cpos="zx", background="w", show_edges=True, smooth_shading=True,)
# Material Params for Wire
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






# contact element top
mapdl.wplane(wn="1", xorig=0.3501, yorig=-1, zorig=1, xxax=1, yxax=-1, zxax=1, xplan=0.3501,
             yplan=1, zplan=1)  # this has the index 4 and won't clash with the coordinate systems later
mapdl.csys("4")

# tool geom
tool_height = 0.2

# square
# width and height are swapped because of the coordinate system
square = mapdl.blc4(xcorner=0, ycorner=0, width=0.5, height=2)
# triangle
tool_k0 = mapdl.k("", 0, 0.6, 0)
tool_k1 = mapdl.k("", tool_height, 0.85, 0)
tool_k2 = mapdl.k("", tool_height, 1.15, 0)
tool_k3 = mapdl.k("", 0, 1.4, 0)
tool = mapdl.a(tool_k0, tool_k1, tool_k2, tool_k3)
tool_slice = mapdl.asba(square, tool)
tool = mapdl.vext(na1=tool_slice, dz=2)
mapdl.csys("0")  # return to normal
mapdl.wpcsys(wn=1, kcn=0)


# Tool is Volume 2, Mesh + Material Properties 
mapdl.esize(0.25)
mapdl.et(2, "SOLID187")
mapdl.type(2)
mapdl.vmesh(2) 

mapdl.mp("EX", 2, 7000000)
mapdl.mp("NUXY", 2, 0.33)

#mapdl.esel("S", "ENAME", vmin=187)
#mapdl.eplot(cpos="zx", background="w", show_edges=True)
#mapdl.esel("S", "ALL")

# contact element bottom, Volume 3
block = mapdl.block(-0.8, -2, -2, 2, -2, 6)
mapdl.esize(0.5)
mapdl.et(3, "SOLID187")
mapdl.type(3)
mapdl.vmesh(3)

mapdl.mp("EX", 3, 7000000)
mapdl.mp("NUXY", 3, 0.33)

# contact
mapdl.nsel("s", "loc", "x", -3, 0.3501 + tool_height + 0.3)
mapdl.nsel("R", "loc", "z", -2, 6)
mapdl.esln("s")
output = mapdl.gcgen("NEW", featureangle=75, splitkey="SPLIT", selopt="SELECT")
print(output)
mapdl.esel("S", "SEC", vmin=3, vmax=15)
mapdl.eplot(style="wireframe", line_width=3)
mapdl.keyopt("CONT", 7, 1)

mapdl.allsel()

# The SOLID185 Element is defined as a 3D tetrahedal with 8 points in total:
#    P+------+O
#    /|     /|
#  M+------+N|
#   |L+ - -| +K
#   |/     |/
#  I+------+J
#
# SOLID186 is very similar, but adds 12 more points to allow finer results. These 12 extra points are not relevant for determining the tilt of the element. For simplicity reasons this explanation uses SOLID 185
#
# See: https://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_elem/Hlp_E_SOLID185.html
# and: https://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_elem/Hlp_E_SOLID186.html
#
# To determine the rotation needed for the local coordinate system we can use 4 edges from each element. Having the global and current element coordinate system in mind we deduce that we can use:
# I -> M, J -> N, L -> P and K -> O
# We can just average the end result to hopefully get a decent approximation of the tilt of each individual element (e.g I->M):
#
# I -> M: Hypotenuse
# U = (I_x, 0, M_z)
# I -> U: Adjacent
# cos tilt = adjacent / hypotenuse

for index, element in enumerate(mapdl.mesh.elem, start=1):
    print(element)
    if len(element) >= 26:
        tilt = calculate_tilt(element)
# Grab the first node
        first_node = int(element[-20:-19])
        mapdl.local(index + 10, "CART", mapdl.queries.nx(first_node),
                    mapdl.queries.ny(first_node), mapdl.queries.nz(first_node), thzx=tilt)
        mapdl.emodif(index, "ESYS", index+10)
        mapdl.csys(0)
        print(index)
    else:
        continue


#mapdl.slashsolu()
#mapdl.nlgeom("ON")
# constraining the bottom contact element (UX = UY = UZ = 0)
mapdl.nsel("s", "loc", "x", -0.8, -2)
mapdl.nsel("R", "loc", "z", -2, 6)
mapdl.d("ALL", "ALL", 0)


# constraining the top contact element (UY = UZ = 0, UX= -displacement)
mapdl.nsel("s", "loc", "x", 0.35, 1)
mapdl.nsel("R", "loc", "z", 1, 3)
mapdl.d("ALL", "UZ", 0)
mapdl.d("ALL", "UY", 0)
mapdl.d("ALL", "UX", -0.6)

# constrain thend areas of the wire in UZ direction
mapdl.da(6, "UZ", 0) 
mapdl.nsel("ALL")
mapdl.nsel("R", "loc", "z", 15, 19)
mapdl.d("ALL", "UX", 0)
mapdl.d("ALL", "UY", 0)
mapdl.d("ALL", "UZ", 0)


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
result = mapdl.result
mapdl.esel("S", "ENAME", vmin=186)
result.plot_principal_nodal_stress(0, "SEQV", lighting=False, background="w", show_edges=True, text_color="k", add_text=False)
mapdl.open_gui()
# mapdl.eplot(show_bounds=True)
