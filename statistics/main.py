from math import sqrt


class Statistics:
    @staticmethod
    def arithmetic_average(values):
        return sum(values)/len(values)
    
    @staticmethod
    def standart_deviation(values):
        arith = Statistics.arithmetic_average(values)
        
        return sqrt( sum([ (value - arith)**2 for value in values ]) / len(values) )


s = Statistics()

print(s.arithmetic_average([3,4,5]))
print(s.standart_deviation([3,4,5]))