import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius**2
    
    def calculate_circumference(self):
        return 2 * math.pi * self.radius

class Triangle:
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    
class Square:
    def __init__(self,side):
        self.side = side
     
    
    def calculate_area(self):
        return self.side **2
    
    def calculate_perimeter(self):
        return 4 * self.side
    
   

# تجربة الأشكال
circle = Circle(5)
print("مساحة الدائرة:", circle.calculate_area())
print("محيط الدائرة:", circle.calculate_circumference())

triangle = Triangle(6, 8, 5, 7, 9)
print("مساحة المثلث:", triangle.calculate_area())
print("محيط المثلث:", triangle.calculate_perimeter())

rectangle = Rectangle(4, 9)
print("مساحة المستطيل:", rectangle.calculate_area())
print("محيط المستطيل:", rectangle.calculate_perimeter())


square = Square(5)
print("مساحة المربع:", square.calculate_area())
print("محيط المربع:", square.calculate_perimeter())
