from random import randint
from art import logo

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS=5

def check_answer(user_guess,actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You guessed it !The answer was {actual_answer}")


def set_difficulty():
    level=input("How many levels do you want? type easy or hard?    ").lower()
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print(logo)
    print("Welcome to Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer=randint(1,100)
    #print(f"psst, the correct answer was {answer}")
    turn = set_difficulty()

    guess=0
    while guess != answer:
        print(f"you have {turn}attempts remaining to guess the number ")
        guess=int(input("Guess the number"))
        turn=check_answer(guess,answer,turn)
        if turn==0:
            print("you are out of guesses, you lose!")
            print( f"the correct answer was {answer}")
            return
        elif guess!=answer:
            print("guess again")
    #print(f"psst, the correct answer was {answer}")
game()
