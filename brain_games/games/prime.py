import random


def prime_check(number):
    i = 0
    for x in range(2, number // 2 + 1):
        if (number % x == 0):
            i += 1
    if i <= 0:
        return "yes"
    else:
        return "no"


RULES = "Answer 'yes' if given number is prime. Otherwise answer 'no'."


def brain_game():
    question = random.randint(1, 50)
    cor_answer = prime_check(question)
    return cor_answer, question
