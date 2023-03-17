#!/usr/bin/env python3
import prompt
from random import randint


def brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    counter = 0
    while counter < 3:
        random_number = randint(1,100)
        print(f"Question: {random_number}")
        answer = prompt.string("Your answer: ")    
        if random_number % 2 == 0 and answer == "yes":
            print("Correct!")
            result = f"Congratulations, {name}!" 
            counter += 1
        elif random_number % 2 != 0 and answer == "no":
            print("Correct!")
            result = f"Congratulations, {name}!"
            counter += 1
        elif random_number % 2 == 0 and answer == "no":
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. Let's try again, {name}!")
            counter = 0
        elif random_number % 2 != 0 and answer == "yes":
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. Let's try again, {name}!")
            counter = 0
        elif answer == "quit":
            result = "The End"
            counter = 3
        else:
            print(f"{answer} is wrong answer ;(. Let's try again, {name}!")
            counter = 0     
    return print(result)


def main():
    brain_even()
    

if __name__ == '__main__':
    main()
