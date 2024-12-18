def kolm(vertices):
    n = len(vertices)  
    area = 0
    
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
        
    return abs(area) / 2
P = (-7, 2)
O = (-3, 5)
R = (3, 3)
S = (3, -5)
vertices = [P, O, R, S]


area = kolm(vertices)
print(f"Nelinurga pindala on: {area} ruutühikut.")
