import numpy as np
import matplotlib.pyplot as plt
import random

class Point:
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
        self._r = ((x**2) + (y**2) + (z**2))**.5

    @property
    def get_rvalue(self):
        return self._r

    def setCoordinate(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._r = ((x**2) + (y**2) + (z**2))**.5

    def getCoordinate(self):
        return self.x, self.y, self.z

    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    def __eq__(self, otherCoordinate):
        if not isinstance(otherCoordinate, Point):
            raise TypeError('You can only compare two circles!')
        if self.get_rvalue == otherCoordinate.get_rvalue:
            return True
        else:
            return False
    
    def __lt__(self, otherCoordinate):
        if not isinstance(otherCoordinate, Point):
            raise TypeError('You can only use the less than operator on two Point objects')
        if self.get_rvalue < otherCoordinate.get_rvalue:
            return True
        else:
            return False

    def __le__(self, otherCoordinate):
        if not isinstance(otherCoordinate, Point):
            raise TypeError('You can only use the less than or equal to operator on two Point objects')
        if self.get_rvalue == otherCoordinate.get_rvalue or self.get_rvalue < otherCoordinate.get_rvalue:
            return True
        else:
            return False

    def __add__(self, otherCoordinate):
        
        x = self.x + otherCoordinate.x
        y = self.y + otherCoordinate.y
        z = self.z + otherCoordinate.z
        
        return Point(x, y, z)
    
    def __iadd__(self, otherCoordinate):
        
        self = self + otherCoordinate
        
        return self

    def asdict(self):
        dictionaryResults = {'x':self.x, 'y':self.y, 'z':self.z}
        return dictionaryResults

class Circle:
    def __init__(self, coordinates, radius):
        self.coordinate = coordinates
        self._radius = radius
    
    @property
    def getRadius(self):
        return self._radius
    
    def setRadius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            print('The value of the radius has to be greater than zero')

    def draw(self):     
        plt.rcParams["figure.figsize"] = [6.00, 3.00]
        plt.rcParams["figure.autolayout"] = True
        fig = plt.figure()
        ax = fig.add_subplot()

        p = self.coordinate
        x, y, z = p.getCoordinate 

        circlePlot = plt.patches.Circle((x,y), radius = self.getRadius, color = 'red')
        ax.add_patch(circlePlot)
        ax.axis('equal')
        ax.set_title(f'(x-{x})^2+(y-{y})^2={self.getRadius}^2')
        plt.show()

class Sphere:
    def __init__(self, coordinates, radius):
        self.coordinates = coordinates
        self._radius = radius
        self._vol = (4/3)*(3.1415)*radius**3

    @property
    def getRadius(self):
        return self._radius

    @property
    def getVolume(self):
        return self._vol
    
    def setRadius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            print('The radius value has to be greater than 0!')

    def __str__(self):
        pcenter = self.coordinates
        return f'The volume of the sphere centered at {pcenter} with a radius of {self.getRadius} is equal to {self.getVolume}'


class CenteredSphere:
    def __init__(self, radius):
        self.coordinates = Point(0, 0, 0)
        self.radius = radius
        self._vol = (4/3)*(3.1415)*radius**3

    @property
    def getVolume(self):
        return self._vol

    def __str__(self):
        return f'The volume of the sphere centered at the origin with a radius of {self.radius} is equal to {self.getVolume}.'

    
p1 = Point(random.randrange(6), random.randrange(6),random.randrange(6))
p2 = Point(random.randrange(6), random.randrange(6),random.randrange(6))
p3 = Point(random.randrange(6), random.randrange(6),random.randrange(6))

r1 = random.randint(1,5)
r2 = random.randint(1,5)
r3 = random.randint(1,5)

s1 = Sphere(p1, r1)
s2 = Sphere(p2, r2)
s3 = Sphere(p3, r3)

listSpheres1 = [s1, s2, s3]

s4 = CenteredSphere(random.randint(5,10))
s5 = CenteredSphere(random.randint(5,10))

listSpheres2 = [s4, s5]

listCombined = listSpheres1 + listSpheres2

for x in listCombined:
    print(x)