class shape:
     def __init__(self, color, is_notfill): 
         self.color = color
         self.is_notfill = is_notfill
         self.area = 0.0
    
class triangle:
    def __init__(self, base, height, color, is_notfill):
        super().__init__(color, is_notfill)
        self.base = base
        self.height = height
        def __init__(self, base, height):
            super().__init__(base, height)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height
    
class square:
    def __init__(self, side, color, is_notfill): 
        super().__init__(color, is_notfill)
        self.side = side
        
        def __init__(self, width, height):
             super().__init__(width, height)  
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class rectangele:
    def __init__(self, length, width, color, is_notfill):
        super().__init__(color, is_notfill)
        self.length = length
        self.width = width 
        def __init__(self, base, height):
            super().__init__(base, height)
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5 * self.base * self.height

class circle:
    def __init__(self, radius, color, is_notfill):
        super().__init__(color, is_notfill)
        self.radius = radius
    def destroy(self):  
        def __init__(self, radius):
          super().__init__(radius)  
        self.radius = radius
