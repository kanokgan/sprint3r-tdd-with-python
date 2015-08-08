import unittest

class TestFirstPatternLeftOperand(unittest.TestCase):
	
	def test_1_should_be_1(self):
		captcha = Captcha(1,1,1,1)
		self.assertEqual('1', captcha.left_operand())
		return False;
	
	def test_2_should_be_2(self):
		captcha = Captcha(1,2,1,1)
		self.assertEqual('2', captcha.left_operand())
		return False;


class TestSecondPatternLeftOperand(unittest.TestCase):
	
	def test_1_should_be_one(self):
		captcha = Captcha(2,1,1,1)
		self.assertEqual('one', captcha.left_operand())



class Captcha():

	def __init__(self, pattern, left, operand, right):
		self.pattern = pattern
		self.left = left

	def left_operand(self):

		if(self.pattern == 2):
			return 'one'

		return str(self.left)
