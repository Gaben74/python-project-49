from random import randint
import math


RULES = "Find the greatest common divisor of given numbers."


def play_game():
    number1 = randint(1, 50)
    number2 = randint(1, 50)
    question = f"{number1} {number2}"
    answer = str(math.gcd(number1, number2))
    return answer, question
