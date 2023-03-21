import random


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def brain_game():
    random_number = random.randint(1, 100)
    cor_answer = "yes" if random_number % 2 == 0 else "no"
    question = str(random_number)
    return cor_answer, question
