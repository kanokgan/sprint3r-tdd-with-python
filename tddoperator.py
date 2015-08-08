class Operator():
	def __init__(self, mode):
		self.mode = mode

	def to_string(self):
		if(self.mode == 1):
			return '+'