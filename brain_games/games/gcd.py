import random
import math


RULES = "Find the greatest common divisor of given numbers."


def play_game():
    number1 = random.randint(1, 50)
    number2 = random.randint(1, 50)
    question = f"{number1} {number2}"
    cor_answer = str(math.gcd(number1, number2))
    return cor_answer, question
