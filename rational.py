from numerical_sets import NumericalSet

class Rational(NumericalSet):
    def __init__(self, rule=None, *values):
        ''' in the rule you put the value that is rational ex: rule=2 for val in values val/2'''
        self.rule = rule
        super().__init__(values)

    def show(self):
        print("{", end=" ")
        for s in self.set:
            if not self.rule:
                print(f"{s}/{1}", end=" ")
            else:
                print(f"{s}/{self.rule}", end=" ")

        print("}")



if __name__ == '__main__':
    r = Rational([1,2,3,4,5,6,7,8,9])
    r.show()
        

