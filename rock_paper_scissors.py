import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_image =[rock, paper, scissors]

user_choice=int(input("What do you choose? Type0 for Rock, 1 for paper, 2 for scissors"))

if user_choice>=0 and user_choice<=2:
    print(game_image[user_choice])
computer_choice=random.randint(0,2)
print(f"computer chose \n {game_image[computer_choice]}")

#if the user inputs other then desired range of input
if user_choice>=3 or user_choice<0:
    print("You typed an invalid option")

elif user_choice==0 and computer_choice==2:
    print("You win")

elif computer_choice==0 and user_choice==2:
    print("You lose")

elif computer_choice>user_choice:
    print("You lose")

elif user_choice>computer_choice:
    print("You win")
elif computer_choice==user_choice:
     print("Its a draw ")
