# creation of multiple object with the same name in python
class Student:
	def __init__(self, name, age, average):
		self.name = name
		self.age = age
		self.average = average
		print(id(self))

	def display(self):
		print(f'Name: {self.name}')
		print(f'Age: {self.age}')
		print(f'Average: {self.average}')

if __name__ == '__main__':
	s1 = Student(name = 'sachin', age = 48, average = 50.6)
	s1.display()
	print(id(s1))
	print()

	s2 = Student(name = 'anurag', age = 24, average = 75.77)
	s2.display()
	print(id(s2))