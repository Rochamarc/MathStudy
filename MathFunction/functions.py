import math
import pandas as pd 


class Exponential:
    def __init__(self, a):
        self.a = a 
    
    def __repr__(self) -> str:
        return f'f(x) = {self.a}^x'
    
    def calculate(self, x):
        ''' Receive the value of x and return the function value '''
        return self.a**x 
    
    def simple_table(self):
        ''' Return a dataframe with x and f(x) values from -2 to 2 '''
        pairs = [ [i, self.calculate(i)] for i in range(2,-3, -1) ]
        return pd.DataFrame(pairs, index=None, columns=['x', 'f(x)'])

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
        ''' Return the value when f(x) = 0 '''
        return (self.b * -1) / self.a 

    def calculate(self, x, verbose=False):
        ''' Receive the value of x and return the function value '''
        return f'f({x}) = {self.a * x + self.b}' if verbose else self.a * x + self.b

    def simple_table(self):
        ''' Return a dataframe with x and f(x) values from -2 to 2 '''
        pairs = []
        for i in range(2, -3, -1):
            pairs.append([i, self.calculate(i)])

        return pd.DataFrame(pairs, index=None, columns=['x', 'f(x)'])

class Quadratic:

    def  __init__(self, a, b, c):
        self.a = a
        self.b = b 
        self.c = c
        self.delta = self.b**2 - (4 * self.a * self.c) 

    @property
    def vertex(self, verbose=False):
        ''' Return the value of the vertex of the function (vertexX, vertexY)'''
        return f"V{( -self.b/2*self.a , self.delta/2*self.a )}" if verbose else [ -self.b/2*self.a , self.delta/2*self.a ]

    @property
    def roots(self):
        ''' Return the values of x that make the function return 0 '''

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


if __name__ == "__main__":
    a = Affine(5,-10)
    print(a)
    print(a.zero)
    print(a.calculate(10))

    print(a.simple_table())

    q = Quadratic(1,-3,2)
    print(q)
    print(q.roots)
    print(q.vertex)

    #
    #
    # Proving sum and product of the roots
    # 

    print(sum(q.roots) == -(q.b)/(q.a)) 
    print(q.roots[0] * q.roots[1] == q.c/q.a) 