from myoperator import Operator
from myoperand import StringOperand
from myoperand import IntOperand


class Captcha():

	def __init__(self, pattern, left, operand, right):
		self.pattern = pattern
		self.left = left
		self.right = right
		self.operand = operand


	def left_operand(self):

		if(self.pattern == 2):
			return StringOperand(self.left).to_string()

		return IntOperand(self.left).to_string()


	def right_operand(self):

		if(self.pattern == 2):
			return StringOperand(self.left).to_string()

		return IntOperand(self.right).to_string()
		


	def operator(self):
		operator = Operator(self.operand)
		return  operator.to_string()

