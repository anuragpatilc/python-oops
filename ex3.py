class Sandesh:
	def __init__(self, branch):
		self.branch = branch

	def display1(self):
		print(f'python class by Sandesh is going on at : {self.branch}')

	def display2(self):
		print(f'java class by Sandesh is going on at : {self.branch}')

if __name__ == '__main__':
	python_trainer = Sandesh(branch = 'vij')
	print(id(python_trainer))
	python_trainer.display1()

	java_trainer = Sandesh(branch = 'btm')
	print(id(java_trainer))
	java_trainer.display2()