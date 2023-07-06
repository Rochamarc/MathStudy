from functions import Affine


class CompositeAffine(Affine):
    def __init__(self, f1:object, f2:object):
        ''' representation of a -> fog(x), so, the second function is the g(x) and the first (x) '''
        a = f1.a * f2.a
        b = f1.a * f2.b + f1.b
        super().__init__(a, b)

    
if __name__ == "__main__":
    a1 = Affine(2,3)
    a2 = Affine(-2,-3)
    c = CompositeAffine(a1,a2)
    print(c)