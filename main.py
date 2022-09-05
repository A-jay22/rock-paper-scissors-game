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

#Write your code below this line 👇
game_images = [rock, paper, scissors]
user = int(input("Select 0 for rock, 1 for paper and 2 for scissors: \n"))
if user >=3 or < 0:
  print("Invalid Number chosen")
print(game_images[user])
computer = random.randint(0, 2)
print(f"computer: {computer}")
print(game_images[user])
if user == computer:
  print("It is a draw")
elif user == 0 and computer == 1:
  print("You lose")
elif user == 0 and computer == 2:
  print("You win")
elif user == 1 and computer == 2:
  print("You win")
elif user == 2 and computer == 1:
  print("You win")
elif user == 2 and computer == 0:
  print("You lose")
elif user == 1 and computer == 0:
  print("You win")
else:
  print("Invalid number chosen")

