import unittest

class TestFirstPatternLeftOperand(unittest.TestCase):
	
	DUMMY_PATTERN = 1
	DUMMY_OPERATOR = 1
	DUMMY_LEFT = 1
	DUMMY_RIGHT = 1

	def test_1_should_be_1(self):
		captcha = Captcha(self.DUMMY_PATTERN, 1, self.DUMMY_OPERATOR, self.DUMMY_RIGHT)
		self.assertEqual('1', captcha.left_operand())
		return False;
	
	def test_2_should_be_2(self):
		captcha = Captcha(self.DUMMY_PATTERN, 2, self.DUMMY_OPERATOR, self.DUMMY_RIGHT)
		self.assertEqual('2', captcha.left_operand())
		return False;


class TestSecondPatternLeftOperand(unittest.TestCase):
	
	DUMMY_PATTERN = 2
	DUMMY_OPERATOR = 1
	DUMMY_LEFT = 1
	DUMMY_RIGHT = 1
	
	def test_1_should_be_one(self):
		captcha = Captcha(self.DUMMY_PATTERN, 1, self.DUMMY_OPERATOR, self.DUMMY_RIGHT)
		self.assertEqual('one', captcha.left_operand())


class TestFirstPatternRightOperand(unittest.TestCase):
	
	DUMMY_PATTERN = 1
	DUMMY_OPERATOR = 1
	DUMMY_LEFT = 1
	DUMMY_RIGHT = 1

	def test_1_should_be_1(self):
		captcha = Captcha(self.DUMMY_PATTERN, self.DUMMY_LEFT, self.DUMMY_OPERATOR, 1)
		self.assertEqual('1', captcha.right_operand())


class TestSecondPatternRightOperand(unittest.TestCase):
	
	DUMMY_PATTERN = 2
	DUMMY_OPERATOR = 1
	DUMMY_LEFT = 1
	DUMMY_RIGHT = 1

	def test_1_should_be_1(self):
		captcha = Captcha(self.DUMMY_PATTERN, self.DUMMY_LEFT, self.DUMMY_OPERATOR, 1)
		self.assertEqual('one', captcha.right_operand())



class Captcha():

	numberStr = ['zero', 'one', 'two', 'tree', 'four', 'five', 'six', 'seven', 'eight', 'nine']

	def __init__(self, pattern, left, operand, right):
		self.pattern = pattern
		self.left = left
		self.right = right

	def left_operand(self):

		if(self.pattern == 2):
			return self.numberStr[self.left]

		return str(self.left)

	def right_operand(self):

		if(self.pattern == 2):
			return self.numberStr[self.right]

		return str(self.right)




























