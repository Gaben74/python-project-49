import prompt


ROUNDS = 3


def play(game):
    print("Welcome to the Brain Games!\n")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!\n")
    print(game.RULES)

    for x in range(ROUNDS):
        cor_answer, question = game.brain_game()
        print("Question:", question)
        answer = prompt.string("Your answer: ")
        if str(cor_answer) != answer:
            print(f"{answer} is wrong answer;(.Correct answer was", cor_answer)
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
