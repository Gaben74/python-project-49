import prompt


ROUNDS = 3


def play(game):
    print("Welcome to the Brain Games!\n")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!\n")
    print(game.RULES)

    for x in range(ROUNDS):
        answer, question = game.play_game()
        print("Question:", question)
        user_answer = prompt.string("Your answer: ")
        if answer != user_answer:
            print(f"{user_answer} is wrong answer;(.Correct answer was", answer)
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f'Congratulations, {name}!')
