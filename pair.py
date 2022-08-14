from numerical_sets import NumericalSet


class OrderedPair:
	def __init__(self, set_a, set_b):
		self.pairs = [ (x,y) for x in set_a.set for y in set_b.set ]

	@property
	def inverse(self):
		return [ (i[-1], i[0]) for i in self.pairs  ]

	@property
	def domain(self):
		res = []
		[ res.append((i[0])) for i in self.pairs if (i[0]) not in res ]
		
		return res 

	@property
	def image(self):
		res = []
		[ res.append((i[-1])) for i in self.pairs if (i[-1]) not in res ]

		return res 

if __name__ == "__main__":
	a = NumericalSet(1,2,3,4,5)
	b = NumericalSet(-5,-4,-3,-2,-1)
	axb = OrderedPair(a,b)
	print(axb.pairs)
	print("\n")
	print(axb.inverse)

	print("\n\n")
	print(axb.domain)
	print("\n")
	print(axb.image)