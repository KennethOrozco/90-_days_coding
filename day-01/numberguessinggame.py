import random

#Generate random number between 1 and 100.
random_integer = random.randint(1,100)

#make a loop to calculate the amount of guesses.
tries = 0


while True:
    number = int(input("Pick a number bewtween 1 and 100: "))
    tries += 1
    if number == random_integer:
        print(f"Correct! you got it in {tries} guesses.")
        break
    elif number > random_integer:
        print(f"Too high!")
    else:
        print(f"Too low!")