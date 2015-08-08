from random import randint

class Randomizer():
	def __init__(self):
		pass

	def random_pattern(self):
		return randint(1,2)

	def random_operator(self):
		return randint(1,3)

	def random_operand(self):
		return randint(0,9)