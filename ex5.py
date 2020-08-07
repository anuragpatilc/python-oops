# parametrized constructor

class Calcluator:
	def __init__(self, a, b ):
		self.a = a
		self.b = b

	def add(self):
		self.result = self.a + self.b

	def display(self):
		print(f'the added result of: {self.a} and {self.b} is {self.result}')

if __name__ == '__main__':
	c = Calcluator(a = 20, b = 10)
	c.add()
	c.display()
