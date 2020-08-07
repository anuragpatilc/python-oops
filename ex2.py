class Demo:
	def __init__(self):
		print('constructor is executed')

	def display(self):
		print('instance method is executed')

if __name__ == '__main__':
	d1 = Demo()
	d2 = Demo()
	d3 = Demo()

	d1.display()
	d1.display()
	