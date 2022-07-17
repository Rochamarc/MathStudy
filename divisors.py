class Divisor:
    def __call__(self, value):
        res = []

        for i in range(1000000):
            if 'int' in str(type(i / value)):
                res.append(i)

        return res


a = Divisor()
print(a(2))

