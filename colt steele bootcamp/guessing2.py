import random

random_number = random.randint(1,10)  # numbers 1 - 10

# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

while True:
    guess = int(input("Pick a random number between 1-10 "))
    if guess < random_number:
        print ("Too low, pick again. ")
    elif guess > random_number:
        print("Too high, pick again. ")
    else:
        print(f"You picked the correct number, which is {guess}")
        play_again = input("Do you want to play again (y/n)? ")
        if play_again == "y":
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thanks for playing! ")
            break
