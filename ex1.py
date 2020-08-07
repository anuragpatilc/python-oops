class Demo:
	def __init__(self):
		print('the constructor is executed')
	def display(self):
		print('the instance method is executed')

if __name__ == '__main__':
	d = Demo()
	d.display()