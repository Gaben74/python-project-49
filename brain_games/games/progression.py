from random import randrange


RULES = "What number is missing in the progression?"


def make_progression():
    number = randrange(1, 50, 1)
    step = randrange(1, 10, 1)
    length = randrange(5, 11)
    progression = []
    for x in range(length):
        progression.append(number)
        number += step
    return progression


def play_game():
    progression = make_progression()
    number_for_question = randrange(len(progression))
    answer = str(progression[number_for_question])
    progression[number_for_question] = '..'
    question = ' '.join(map(str, progression))
    return answer, question
