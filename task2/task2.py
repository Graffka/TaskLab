from skspatial.objects import Line
from skspatial.objects import Sphere
from skspatial.plotting import plot_3d
import re
import sys

def CenterCoord(String):  #определяем координаты центра сферы
    f = open(String)
    file = f.read()

    index_center = file.find("center")
    index_radius = file.find("radius")
    index_line = file.find("line")
    mass = (re.findall(r'\d*\.?\d+', file))
    # mass1=mass[0:3]
    global mass_center
    if index_center < index_radius and index_center < index_line:
        mass_center = mass[0:3]
    elif index_center > index_radius and index_center > index_line:
        mass_center = mass[7:10]
    elif index_radius<index_line:
        mass_center = mass[1:4]
    else: mass_center=mass[6:9]


    return mass_center

def Radius(String): #находим радиус сферы

    f=open(String)
    file=f.read()

    index_center =file.find("center")
    index_radius =file.find("radius")
    index_line =file.find("line")
    mass = (re.findall(r'\d*\.?\d+', file))

    if index_radius < index_center and index_radius < index_line:
        mass_radius = mass[0:1]
    elif index_radius > index_center and index_radius > index_line:
        mass_radius = mass[9:10]
    elif index_center<index_line:
        mass_radius = mass[3:4]
    else: mass_radius=mass[6:7]

    return mass_radius

def LineAB(String): #находим линию

    f=open(String)
    file=f.read()

    index_center =file.find("center")
    index_radius =file.find("radius")
    index_line =file.find("line")
    mass = (re.findall(r'\d*\.?\d+', file))
    print(mass)

    if index_line < index_center and index_line < index_radius:
        mass_lin = mass[0:6]
    elif index_line > index_center and index_line > index_radius:
        mass_lin = mass[4:10]
    elif index_radius<index_line:
        mass_lin = mass[3:9]
    else: mass_lin=mass[1:7]

    return mass_lin

def Point (String):
    sphere = Sphere([0, 0, 0], 1)
    line = Line([0, 0, 0], [1, 1, 1])

    point_a, point_b = sphere.intersect_line(line)
    finalStr=str(point_a)+'\n'+str(point_b)
    plot_3d(
        line.plotter(t_1=-1, c='k'),
        sphere.plotter(alpha=0.2),
        point_a.plotter(c='r', s=100),
        point_b.plotter(c='r', s=100),
    )
    return finalStr




if __name__ == "__main__":
    print(Point(*sys.argv[1:]))