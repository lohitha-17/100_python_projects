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
game_image = [rock, paper, scissors]

user_choice = int(input("what you want to choose?\n 0 for rock \n 1 for paper \n 2 for scissors\n "))

if user_choice >=0 and user_choice <2:
        print(game_image[user_choice])

computer_choice = random.randint(0,2)
print("computer choice: ")
print(game_image[computer_choice])
if user_choice >=3 or computer_choice <0:
    print("Enter a valid choice")

elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and computer_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a tie!")