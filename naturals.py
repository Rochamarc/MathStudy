from numerical_sets import NumericalSet

class Natural(NumericalSet):
	def __init__(self, rule=None, val=None, infinite=False, n=None, *values):
		self.rule = rule 
		self.infinite = infinite
		self.n = n
		self.val = val 
		super().__init__(*self.get_values())

	def get_values(self):
		if not self.rule:
			return [ i for i in range(1000) ]
		if 'multiply' in self.rule:
			return [ (i+1) * self.val for i in range(self.n) ]
		if 'odd' in self.rule:
			return [ i for i in range(1, (self.n)*2) if i % 2 != 0 ]

	def __str__(self):
		s = str(self.set[0:10]).replace('[', '').replace(']', '')
		if self.infinite:
			return '{' + s + ', ...}'
		return '{' + s + '}'

if __name__ == '__main__':
	m_4 = Natural(rule='multiply', val=4, n=12)
	m_6 = Natural(rule='multiply', val=6, n=7)
	m_12 = Natural(rule='multiply', val=12, n=5)
	odd = Natural('odd', n=8)

	print(m_4)
	print(m_6)
	print(m_12)
	print(odd)


	x = m_4.unity(m_6)
	x = x.unity(m_12)
	x = x.unity(odd)

	print(x) 

