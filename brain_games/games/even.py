import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def play_game():
    random_number = random.randint(1, 100)
    cor_answer = is_even(random_number)
    cor_answer = "yes" if cor_answer is True else "no"
    question = str(random_number)
    return cor_answer, question
