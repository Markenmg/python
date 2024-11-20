class Shape:
    def __init__(self, dim1=None, dim2=None):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        raise NotImplementedError("")

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(base, height)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape): 
    def __init__(self, width, height):
        super().__init__(width, height)  
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):  
    def __init__(self, radius):
        super().__init__(radius)  
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)


triangle = Triangle(10, 5)
rectangle = Rectangle(4, 6)
circle = Circle(3)

print(f"Triangle area: {triangle.area()}")  
print(f"Rectangle area: {rectangle.area()}")  
print(f"Circle area: {circle.area():.2f}")  
