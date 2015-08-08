class Captcha():

	numberStr = ['zero', 'one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	operatorStr = ['+', '*', '-']

	def __init__(self, pattern, left, operand, right):
		self.pattern = pattern
		self.left = left
		self.right = right
		self.operand = operand


	def left_operand(self):

		if(self.pattern == 2):
			return self.numberStr[self.left]

		return str(self.left)


	def right_operand(self):

		if(self.pattern == 2):
			return self.numberStr[self.right]

		return str(self.right)
		

	def operator(self):

		return self.operatorStr[self.operand - 1]

