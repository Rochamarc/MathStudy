#
#
#

from pair import Pair

class AffineFunction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.f_x_ = f'{self.a}x + {self.b}'
        self.points = [ Pair(x, x*self.a + self.b) for x in range(-3,) if   ]

    def plot(self):

        

