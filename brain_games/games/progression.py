import random


RULES = "What number is missing in the progression?"


def make_progression():
    number = random.randrange(1, 50, 1)
    step = random.randrange(1, 10, 1)
    length = random.randrange(5, 11)
    progression = []
    for x in range(length):
        progression.append(number)
        number += step
    return progression


def play_game():
    progression = make_progression()
    number_for_question = random.randrange(len(progression))
    cor_answer = str(progression[number_for_question])
    progression[number_for_question] = '..'
    question = ' '.join(map(str, progression))
    return cor_answer, question
