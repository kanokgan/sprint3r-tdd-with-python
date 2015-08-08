class Operand():
	def __init__(self):
		pass

	def to_string(self):
		raise Exception('MUST BE IMPLEMENT')


class StringOperand(Operand):

	numberStr = ['zero', 'one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine']

	def __init__(self, num):
		self.num = num

	def to_string(self):
		return self.numberStr[self.num]


class IntOperand(Operand):

	def __init__(self, num):
		self.num = num

	def to_string(self):
		return str(self.num)