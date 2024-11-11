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

# This is in the function context with domain, codomain and image
class OrderedPair:	
	def __init__(self, set_a, set_b):
		self.pairs = [ (x,y) for x in set_a.set for y in set_b.set ]

	@property
	def inverse(self):
		return [ i[::-1] for i in self.pairs  ]

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

	od = OrderedPair([1,2,3], [4,5,6])
	print(od) 
