class Operator():

	operatorStr = ['+', '*', '-']

	def __init__(self, mode):
		self.mode = mode

	def to_string(self):
		return self.operatorStr[self.mode - 1]