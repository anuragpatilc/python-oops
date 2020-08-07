class Employee:

	def __init__(sandesh, name, age, marks):
		sandesh.name = name
		sandesh.age = age
		sandesh.marks = marks
		print(id(sandesh))

	def display(akash):
		print(id(akash))
		print(akash.name)
		print(akash.age)
		print(akash.marks)

if __name__ == '__main__':
	e1 = Employee(name= 'anurag', age = 23, marks = 50)
	print(id(e1))
	e1.display()