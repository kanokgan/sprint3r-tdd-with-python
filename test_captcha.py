import unittest

class TestFirstPatternLeftOperand(unittest.TestCase):
	
	def test_1_should_be_1(self):
		captcha = Captcha(1,1,1,1)
		self.assertEqual('1', captcha.left_operand())
		return False;


class Captcha():

	def __init__(self, pattern, left, operand, right):
		pass

	def left_operand(self):
		return '1'