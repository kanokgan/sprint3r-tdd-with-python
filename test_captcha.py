import unittest
from app import app
from mycaptcha import Captcha
from myoperator import Operator
from myoperand import StringOperand
from myoperand import IntOperand
from myrandomizer import Randomizer
from CaptchaController import CaptchaController

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


class TestStringOperandClass(unittest.TestCase):

	def test_input_1_should_be_one(self):
		stringOperand = StringOperand(1)
		self.assertEqual('one', stringOperand.to_string())

	def test_input_2_should_be_two(self):
		stringOperand = StringOperand(2)
		self.assertEqual('two', stringOperand.to_string())

class TestIntOperandClass(unittest.TestCase):

	def test_input_1_should_be_1(self):
		intOperand = IntOperand(1)
		self.assertEqual('1', intOperand.to_string())

	def test_input_2_should_be_2(self):
		intOperand = IntOperand(2)
		self.assertEqual('2', intOperand.to_string())


class TestRandomizerClass(unittest.TestCase):

	def test_pattern_should_return_between_1_and_2(self):
		self.assertTrue(1 <= Randomizer().random_pattern() <= 2)

	def test_operator_shoud_return_between_1_and_3(self):
		self.assertTrue(1 <= Randomizer().random_operator() <= 3)

	def test_operand_shoud_return_between_0_and_9(self):
		self.assertTrue(0 <= Randomizer().random_operand() <= 9)



class TestCaptchaAPI(unittest.TestCase):
	
	def test_it_should_return_200(self):
		self.app = app.test_client()
		response = self.app.get('/captcha')
		self.assertEqual(response.status_code, 200)


class TestCapchaController(unittest.TestCase):

	def test_should_be_return_valid_json(self):
		captcha_controller = CaptchaController()
		captcha_controller.captcha = Captcha(1,1,1,1)
		self.assertEqual('{"left": "1", "operator": "1", "right": "1"}', captcha_controller.to_json())

# class TestCaptchaControllerRandomizer(unittest.TestCase):
# 	def test_get(self):

# 		stubRandomizer = Randomizer()

# 		def stub_pattern():
# 			return 1

# 		def stub_operand():
# 			return 1

# 		def stub_operator():
# 			return 1

# 		stubRandomizer.pattern = stub_pattern
# 		stubRandomizer.operand = stub_operator
# 		stubRandomizer.operator = stub_operand
		

# 		captchaController = CaptchaController()


# 		captchaController.Randomizer = stubRandomizer

# 		assertEqual('{"left": "1", "operator": "1", "right": "1"}', captchaController.get())




































