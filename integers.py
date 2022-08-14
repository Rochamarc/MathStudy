from naturals import Natural

class Integer(Natural):
	def __init__(self, rule=None, val=None, infinite=False, n=None, *values):
		super().__init__(rule=None, val=None, infinite=False, n=None, *values)


if __name__ == "__main__":
	a = Integer()
	print(a)