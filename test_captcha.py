import unittest
from captcha import Captcha
from tddoperator import Operator

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

class TestOperator(unittest.TestCase):
	
	DUMMY_PATTERN = 1
	DUMMY_OPERATOR = 1
	DUMMY_LEFT = 1
	DUMMY_RIGHT = 1

	def test_1_should_be_plus(self):
		captcha = Captcha(self.DUMMY_PATTERN, self.DUMMY_LEFT, 1, self.DUMMY_RIGHT)
		self.assertEqual('+', captcha.operator())

	def test_2_should_be_multiply(self):
		captcha = Captcha(self.DUMMY_PATTERN, self.DUMMY_LEFT, 2, self.DUMMY_RIGHT)
		self.assertEqual('*', captcha.operator())

	def test_3_should_be_minus(self):
		captcha = Captcha(self.DUMMY_PATTERN, self.DUMMY_LEFT, 3, self.DUMMY_RIGHT)
		self.assertEqual('-', captcha.operator())


class TestOperatorClass(unittest.TestCase):

	def test_1_should_be_plus(self):
		operator = Operator(1)
		self.assertEqual('+', operator.to_string())

	def test_2_should_be_multiply(self):
		operator = Operator(2)
		self.assertEqual('*', operator.to_string())

	def test_3_should_be_minus(self):
		operator = Operator(3)
		self.assertEqual('-', operator.to_string())



