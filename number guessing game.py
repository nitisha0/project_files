import random
number = random.randint(1 , 100)
attempts = 0
while True:
    attempts += 1
    guess = int(input("guess the number : "))
    if (guess < number) :
        print("guess higher!")
    elif (guess > number) :
        print("guess lower!")
    else:
        print(f"you guessed the number in {attempts} attempts .  you won!")
        break
print("thanks for playing")

