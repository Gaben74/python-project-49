import operator
from random import randint, choice


RULES = 'What is the result of the expression?'
OPERATORS = ((operator.add, '+'),
             (operator.sub, '-'),
             (operator.mul, '*'))


def play_game():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    operator_type, operator_text = choice(OPERATORS)
    question = f"{number1} {operator_text} {number2}"
    answer = str(operator_type(number1, number2))
    return answer, question
