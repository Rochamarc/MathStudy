from functions import Exponential

class Exp(Exponential):
    def __init__(self, a, b=0):
        ''' This represents a transformation that a add or subb value does to an exponential function '''
        super().__init__(a)
        self.b = b

    def __repr__(self) -> str:
        sign = '+' if self.b > 0 else ''
        return f"f(x) = {self.a}^x{sign}{self.b}"
    
    def calculate(self, x):
        return super().calculate(x) + self.b 
    

if __name__ == "__main__":
    a = Exponential(2)
    ex = Exp(2,b=-2)


    print(f"This is {a}")
    print(a.simple_table())
    print("\n")
    print(f"This is {ex}")
    print(ex.simple_table())