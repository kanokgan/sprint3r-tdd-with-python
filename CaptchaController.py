class CaptchaController():

	def get(self):
		self.captcha = Captcha(self.randomizer.pattern(), self.randomizer.operand, self.randomizer.operator, self.randomizer.operand)
		return self.to_json()

	def to_json(self):
		return '{"left": "1", "operator": "1", "right": "1"}';