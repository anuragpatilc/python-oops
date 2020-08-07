# crating of  object
class Student:
	def __init__(self):
		self.name = 'Sachin'
		self.age = 48
		self.average = 50.6

	def display(self):
		print(f'Name: {self.name}')
		print(f'age: {self.age}')
		print(f'average: {self.average}')

if __name__ == '__main__':
	s1 = Student()
	s1.display()