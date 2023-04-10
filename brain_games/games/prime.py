import random


def is_prime(number):
    i = 0
    for x in range(2, number // 2 + 1):
        if (number % x == 0):
            i += 1
    if i <= 0:
        return True
    else:
        return False


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def play_game():
    question = random.randint(1, 50)
    cor_answer = is_prime(question)
    cor_answer = "yes" if cor_answer is True else "no"
    return cor_answer, question
