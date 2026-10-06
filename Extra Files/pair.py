class Pair:
	def __init__(self, x: any, y: any):
		self.x = x 
		self.y = y 

	def __str__(self) -> str:
		return "{" + str(self.pair) + "}"

	def __repr__(self) -> str:
		return "{" + str(self.pair) + "}"

	@property
	def pair(self) -> tuple:
		return (self.x, self.y)
	
class OrderedPair2:
	def __init__(self, *pairs: list):
		self.pairs = pairs

	def __str__(self) -> str:
		string = ""

		for pair in enumerate(self.pairs):
			pair, index = pair[-1], pair[0]
			string += f"({pair[0]}, {pair[-1]})"

			if (index + 1) != len(self.pairs):
				string += ", "

		return "S = {" + string + "}"

class OrderedPair(OrderedPair2):	
	def __init__(self, set_a: list[any], set_b: list[any]):
		self.possibilities = [ (x,y) for x in set_a for y in set_b ]
		super().__init__(*self.possibilities)

	@property
	def inverse(self) -> list:
		return [ i[::-1] for i in self.pairs  ]

	@property
	def domain(self) -> list:
		res = [ pair[0] for pair in self.pairs ]

		return list(set(res)) 

	@property
	def image(self):
		res = [ pair[-1] for pair in self.pairs ]

		return list(set(res)) 

if __name__ == "__main__":
	p = OrderedPair(['a','b','c'], ['d','e','f'])
	print(p)