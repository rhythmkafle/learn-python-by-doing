import random

secret = random.randint(1,100)

no_of_guesses = 0

while True and no_of_guesses<=7:
    no_of_guesses = no_of_guesses + 1
    if no_of_guesses == 7:
        print("Too many guesses. You fail!")
        break
    user_input = int(input("Enter a number, 1-100: "))   
    if user_input == secret:
        print("Congratulations, you guessed the right number")
        print("Guessed in %d guesses" % no_of_guesses)
        break
    elif user_input > secret:
        print("Nope!, Try again. A little lower this time...")
    elif user_input < secret:
        print("Nope!, Try again. A little higher this time...")
        