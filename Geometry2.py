#  File: Geometry.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import math
import sys
import os
os.system('cls')

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return f'({str(self.x)}, {str(self.y)}, {str(self.z)})'

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)
  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-6
    return (
        (abs(self.x - other.x) < tol) and \
        (abs(self.y - other.y) < tol) and \
        (abs(self.z - other.z) < tol)
        )

class Sphere (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1):
    self.center = Point(x,y,z)
    self.radius = float(radius)
  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return f'Center: ({str(self.center.x)}, {str(self.center.y)}, {str(self.center.z)}), Radius: {str(self.radius)}'
  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return 4*math.pi*(self.radius**2)
  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return (4/3)*math.pi*(self.radius**3)
  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return self.center.distance(p) < self.radius
  def is_outside_point (self,p):
    #unchecked
    return self.center.distance(p) > self.radius
  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
    R = [-other.radius,other.radius]
    a=0
    b=0
    c=0
    for i in R:
        a = i + other.center.x
        b = 0
        c = 0
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_inside_point(spherical_corner):
            return False
    for j in R:
        a = 0
        b = j + other.center.y
        c = 0
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_inside_point(spherical_corner):
            return False
    for k in R:
        a = 0
        b = 0
        c = k + other.center.z
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_inside_point(spherical_corner):
            return False

    #dist_center = self.center.distance(other.center)
    #return (dist_center + other.radius) < self.radius
    return True
  def is_outside_sphere (self, other):
    R = [-other.radius,other.radius]
    a=0
    b=0
    c=0
    for i in R:
        a = i + other.center.x
        b = 0
        c = 0
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_outside_point(spherical_corner):
            return False
    for j in R:
        a = 0
        b = j + other.center.y
        c = 0
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_outside_point(spherical_corner):
            return False
    for k in R:
        a = 0
        b = 0
        c = k + other.center.z
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_outside_point(spherical_corner):
            return False
    return True
  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are strictly 
  # inside the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    L = [-a_cube.side/2,a_cube.side/2]
    for i in L:
        for j in L:
            for k in L:
                a=i+a_cube.center.x
                b=j+a_cube.center.y
                c=k+a_cube.center.z
                a_cube_corner = Point(a,b,c)
                print(a_cube_corner)
                if not self.is_inside_point(a_cube_corner):
                    print(a_cube_corner)
                    return False
    
    return True
  def is_outside_cube (self, a_cube):
    #unchecked
    L = [-a_cube.side/2,a_cube.side/2]
    for i in L:
        for j in L:
            for k in L:
                a=i+a_cube.center.x
                b=j+a_cube.center.y
                c=k+a_cube.center.z
                a_cube_corner = Point(a,b,c)
                print(a_cube_corner)
                if not self.is_outside_point(a_cube_corner):
                    print(a_cube_corner)
                    return False
    
    return True
  # determine if another Sphere intersects this Sphere
  # other is a Sphere object
  # two spheres intersect if they are not strictly inside
  # or not strictly outside each other
  # returns a Boolean
  def does_intersect_sphere (self, other):
    #dist_center = self.center.distance(other.center)
    #inside = (dist_center + other.radius) < self.radius
    #outside = (dist_center - other.radius) > self.radius
    #print(inside)
    #print(outside)
    #return (not inside) and (not outside)
    return  not (self.is_inside_sphere(other)) and not (self.is_outside_sphere(other))

  # determine if a Cube intersects this Sphere
  # the Cube and Sphere intersect if they are not
  # strictly inside or not strictly outside the other
  # a_cube is a Cube object
  # returns a Booleanr4
  def does_intersect_cube (self, a_cube):
    #unchecked

    #self.is_inside_cube(a_cube)
    #self.is_outside_cube(a_cube)
    return  not (self.is_inside_cube(a_cube)) and not (self.is_outside_cube(a_cube))
 

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self):
    #unchecked
    a_cube = Cube()
    a_cube.center = self.center
    a_cube.side= self.radius/math.sqrt(3)
    return a_cube

class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0, y = 0, z = 0, side = 1):
    self.center = Point(x,y,z)
    self.side = float(side)

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return f'Center: ({str(self.center.x)}, {str(self.center.y)}, {str(self.center.z)}), Side: {str(self.side)}'

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return 6*(self.side**2)

  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return self.side**3

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    return\
        ((abs(p.x - self.center.x)) < (self.side/2 )) and\
        ((abs(p.y - self.center.y)) < (self.side/2 )) and\
        ((abs(p.z - self.center.z)) < (self.side/2 ))

  def is_outside_point (self, p):
    return\
        ((abs(p.x - self.center.x)) > (self.side/2 )) or\
        ((abs(p.y - self.center.y)) > (self.side/2 )) or\
        ((abs(p.z - self.center.z)) > (self.side/2 ))
  # determine if a Sphere is strictly inside this Cube 
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    R = [-a_sphere.radius,a_sphere.radius]
    a=0
    b=0
    c=0
    for i in R:
        a = i + a_sphere.center.x
        b = 0
        c = 0
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_inside_point(spherical_corner):
            return False
    for j in R:
        a = 0
        b = j + a_sphere.center.y
        c = 0
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_inside_point(spherical_corner):
            return False
    for k in R:
        a = 0
        b = 0
        c = k + a_sphere.center.z
        spherical_corner = Point(a,b,c)
        print(spherical_corner)
        if not self.is_inside_point(spherical_corner):
            return False
    return True

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean

  def is_inside_cube (self, other):
    L = [-other.side/2,other.side/2]
    for i in L:
        for j in L:
            for k in L:
                a=i+other.center.x
                b=j+other.center.y
                c=k+other.center.z
                other_cube_corner = Point(a,b,c)
                #print(other_cube_corner)
                if not self.is_inside_point(other_cube_corner):
                    #print(other_cube_corner)
                    return False
    
    return True
  def is_outside_cube (self, other):
    L = [-other.side/2,other.side/2]
    for i in L:
        for j in L:
            for k in L:
                a=i+other.center.x
                b=j+other.center.y
                c=k+other.center.z
                other_cube_corner = Point(a,b,c)
                #print(other_cube_corner)
                if not self.is_outside_point(other_cube_corner):
                    #print(other_cube_corner)
                    return False
    
    return True
  # determine if another Cube intersects this Cube
  # two Cube objects intersect if they are not strictly
  # inside and not strictly outside each other
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    return  not (self.is_inside_cube(other)) and not (self.is_outside_cube(other))

  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other):
    return None

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    a_sphere = Sphere()
    a_sphere.center = self.center
    a_sphere.radius = self.side
    return a_sphere

class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0, y = 0, z = 0, radius = 1, height = 1):
    return None

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return None

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return None

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return None

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p):
    return None

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
    return None

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are inside
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
    return None

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other):
    return None

def main():
    #p=Point(x=1.99,y=-1.99,z=-1.99)
    sphereA = Sphere(0,0,0,10)
    sphereB = Sphere(5,1,2,3)
    #cubeA = Cube(x=0,y=0,z=1,side=8)
    #cubeB = Cube(x=3,y=10,z=.50,side=8)
    print(sphereA.is_inside_sphere(sphereB))
    #print(cubeA.center.x)    
    #print(cubeA.center.y)
    #print(cubeA.center.z)
    #print(cubeA.side)
    #print(cubeA)
    #print(cubeA.area())
    #print(cubeA.volume())
    #print(cubeA.is_inside_point(p))


  # read data from standard input

  # read the coordinates of the first Point p

  # create a Point object 

  # read the coordinates of the second Point q

  # create a Point object 

  # read the coordinates of the center and radius of sphereA

  # create a Sphere object 

  # read the coordinates of the center and radius of sphereB

  # create a Sphere object

  # read the coordinates of the center and side of cubeA

  # create a Cube object 

  # read the coordinates of the center and side of cubeB

  # create a Cube object 

  # read the coordinates of the center, radius and height of cylA

  # create a Cylinder object 

  # read the coordinates of the center, radius and height of cylB

  # create a Cylinder object

  # print if the distance of p from the origin is greater 
  # than the distance of q from the origin

  # print if Point p is inside sphereA

  # print if sphereB is inside sphereA

  # print if cubeA is inside sphereA

  # print if sphereA intersects with sphereB

  # print if cubeB intersects with sphereB

  # print if the volume of the largest Cube that is circumscribed 
  # by sphereA is greater than the volume of cylA

  # print if Point p is inside cubeA

  # print if sphereA is inside cubeA

  # print if cubeB is inside cubeA

  # print if cubeA intersects with cubeB

  # print if the intersection volume of cubeA and cubeB
  # is greater than the volume of sphereA

  # print if the surface area of the largest Sphere object inscribed 
  # by cubeA is greater than the surface area of cylA

  # print if Point p is inside cylA

  # print if sphereA is inside cylA

  # print if cubeA is inside cylA


if __name__ == "__main__":
  main()