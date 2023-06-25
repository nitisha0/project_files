                                    #rock paper scissors game
import random
user_action = input("enter your choice (rock , paper , scissors, ) : ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\n you choose {user_action} , computer choose {computer_action}. \n ")

if user_action == computer_action:
    print(f"both players choose same option! its a tie. ")
elif user_action == "rock":
    if computer_action == "scissors":
        print("rock smashes scissors! you won. computer lose.")
    else:
        print("paper covers rock! computer won. you lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("paper covers rock! you won. computer lose.")
    else:
        print("scissors cuts paper! computer won. you lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("scissors cuts paper! you won. computer lose. ")
    else:
        print("rock smashes scissors! computer won. you lose.")