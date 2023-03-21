import random


RULES = 'What is the result of the expression?'


def brain_game():
    operator = ['+', '-', '*']
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    oper = random.choice(operator)
    question = f"{number1} {oper} {number2}"
    if '+' == oper:
        cor_answer = str(number1 + number2)
    if '-' == oper:
        cor_answer = str(number1 - number2)
    if '*' == oper:
        cor_answer = str(number1 * number2)
    return cor_answer, question
