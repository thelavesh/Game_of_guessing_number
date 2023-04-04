import random

# generate random number between 1 and 100
number = random.randint(1, 100)

# initialize variables
guesses = 0
correct = False

# loop until user guesses the correct number
while not correct:
    # ask user for guess
    guess = int(input("Guess a number between 1 and 100: "))
    guesses += 1
    
    # provide feedback on guess
    if guess == number:
        print("Congratulations, you guessed the number in", guesses, "guesses!")
        print("Well done! You correctly guessed the number.")
        correct = True
    elif guess < number:
        print("Too low, try again.")
    else:
        print("Too high, try again.")
