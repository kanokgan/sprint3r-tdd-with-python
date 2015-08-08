from flask import Flask 
from mycaptcha import Captcha
from myoperator import Operator
from myoperand import StringOperand
from myoperand import IntOperand
from myrandomizer import Randomizer

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello World"

@app.route('/captcha')
def captcha():
	return 'hello world'


if __name__ == '__main__':
	app.debug = True
	app.run()