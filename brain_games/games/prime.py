from random import randint


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
    question = randint(1, 50)
    answer = is_prime(question)
    answer = "yes" if answer is True else "no"
    return answer, question
