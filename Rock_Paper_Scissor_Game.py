# This is a rock, paper and scissor game between user and computer

import random
options= ["Rock","Paper","Scissor"]
random.choice = random.choice(options)

user_choice = str(input("Enter your choice{Rock, Paper, Scissor} :"))

if user_choice == "Rock" and random.choice == "Paper":
    print(f"Computer won! Computer Choosed: {random.choice}")
elif user_choice == "Paper" and random.choice == "Rock":
    print(f"You won! Computer Choosed: {random.choice}")
elif user_choice == "Paper" and random.choice == "Scissor":
    print(f"Computer won! Computer Choosed: {random.choice}")
elif user_choice == "Scissor" and random.choice == "Paper":
    print(f"You won! Computer Choosed: {random.choice}")
elif user_choice == "Scissor" and random.choice == "Rock":
    print(f"Computer won! Computer Choosed: {random.choice}")
elif user_choice == "Rock" and random.choice =="Scissor":
    print(f"You won! Computer Choosed: {random.choice}")
elif user_choice == random.choice :
    print(f"Tie! Computer Choosed: {random.choice}") 
else:
    print("Invalid Choice!")