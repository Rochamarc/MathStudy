import math
#
#
#

class Divison:
    def __call__(self, dividend, divisor):
        res = dividend/divisor

        return math.floor(res) 


d = Divison()
print(d(10,2))
print(d(4,2))
print(d(2,4))
