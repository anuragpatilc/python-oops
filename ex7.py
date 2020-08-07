class Employee:

	def __init__(self):
		print('construction is executing')

if __name__ == '__main__':
	e = Employee()
	e.__init__()
	e.__init__()