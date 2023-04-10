from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def play_game():
    random_number = randint(1, 100)
    answer = is_even(random_number)
    answer = "yes" if answer is True else "no"
    question = str(random_number)
    return answer, question
