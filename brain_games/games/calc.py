import operator
import random


RULES = 'What is the result of the expression?'
OPERATORS = ((operator.add, '+'),
             (operator.sub, '-'),
             (operator.mul, '*'))


def play_game():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    oper_type, oper_text = random.choice(OPERATORS)
    question = f"{number1} {oper_text} {number2}"
    cor_answer = str(oper_type(number1, number2))
    return cor_answer, question
