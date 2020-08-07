# The name of the self may change into any name as user wants  the program works fine no problem
class Student:
	def __init__(anurag, name, age, average):
		anurag.name = name
		anurag.age = age
		anurag.average = average
		print(id(anurag))

	def display(anurag):
		print(anurag.name, anurag.age, anurag.average)

if __name__ == '__main__':
	s = Student(name = 'anurag', age = 24, average = 99)
	print(id(s))
	s.display()