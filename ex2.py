class Cricketer:
	def __init__(self, name, age, average):
		self.name = name
		self.age = age
		self.average = average

	def display(self):
		print(f'Name: {self.name}')
		print(f'Age: {self.age}')
		print(f'Average: {self.average}')

if __name__ == '__main__':
	c = Cricketer(name = 'sachin', age = 48, average = 50.6)
	c.display()