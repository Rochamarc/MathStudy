import math

class Affine:
    def __init__(self, a, b):
        self.a = a 
        self.b = b
    
    def __repr__(self):
        if self.b > 0:
            b = f"+{self.b}"
        else:
            b = f"{self.b}"

        return f"f(x) = {self.a}x {b}"

    @property
    def zero(self):
        return (self.b * -1) / self.a 

class Quadratic:

    def  __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c
        self.delta = self.b**2 - (4 * self.a * self.c) 
        
    @property
    def roots(self):        
        if self.delta < 0:
            return [] 

        if self.delta == 0:
            return [ (-self.b + 0)/ 2 * self.a ]

        x_1 = ( -self.b + math.sqrt(self.delta) )/ 2 * self.a
        x_2 = ( -self.b - math.sqrt(self.delta) )/ 2 * self.a
        return [x_1, x_2]
        
    def __repr__(self):
        if self.b > 0:
            b = f"+{self.b}x"
        else:
            b = f"{self.b}x"

        if self.c > 0:
            c = f"+{self.c}"
        else:
            c = f"{self.c}"

        return f"f(x) = {self.a}x² {b} {c}"

a = Affine(5,-10)
print(a)
print(a.zero)

q = Quadratic(1,-3,2)
print(q)
print(q.roots)