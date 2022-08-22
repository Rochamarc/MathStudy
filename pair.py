from Sets.numerical_sets import NumericalSet

class Pair:
	def __init__(self, x, y):
		self.x = x 
		self.y = y 
		self.pair = (self.x, self.y)

	def __str__(self):
		return "{" + str(self.pair) + "}"

	def __repr__(self) -> str:
		return "{" + str(self.pair) + "}"

class OrderedPair2:
	def __init__(self, *pairs):
		self.pairs = [ pairs ]

	def __str__(self):
		return "S = {" + str([ pair for pair in self.pairs ]) + "}"

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
	p1 = Pair(1,-3)
	p2 = Pair(2,0)
	p3 = Pair(3,3)

	od = OrderedPair2(p1,p2,p3)
	print(od) 

	"""
	a = NumericalSet(1,2,3,4,5)
	b = NumericalSet(-5,-4,-3,-2,-1)
	axb = OrderedPair(a,b)
	print(axb.pairs)
	print("\n")
	print(axb.inverse)0

	print("\n\n")
	print(axb.domain)
	print("\n")
	print(axb.image)
	"""