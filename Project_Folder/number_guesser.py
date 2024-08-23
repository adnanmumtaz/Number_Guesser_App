import random

upper_limit = input("Enter a number: ")
if upper_limit.isdigit():
    upper_limit = int(upper_limit)

    if upper_limit <= 0:
        print("Please enter a number greater than 0")
        quit()
else:
    print("Please enter any digit next time")
    quit()

random_number = random.randrange(1, upper_limit)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Enter a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Pleae enter any digit next time")
        continue

    if user_guess == random_number:
        print("You got it right")
        break
    elif user_guess > random_number:
        print("You are above the number.")
    else:
        print("You are below the number.")

print("You guessed it in", guesses, "times")
