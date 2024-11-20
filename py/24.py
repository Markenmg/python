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
        
class square:
    def __init__(self, side, color, is_notfill): 
        super().__init__(color, is_notfill)
        self.side = side
class rectangele:
    def __init__(self, length, width, color, is_notfill):
        super().__init__(color, is_notfill)
        self.length = length
        self.width = width
class circle:
    def __init__(self, radius, color, is_notfill):
        super().__init__(color, is_notfill)
        self.radius = radius
    def (f"it is circle, are:{3.14*self.radius*self . radius}, cicumference:{2*3.14*self})