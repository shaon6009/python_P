import random

while True:
    top_of_range = input("Type a number: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range > 0:
            break
        else:
            print("Please type a number greater than 0.")
    else:
        print("Invalid input! Please type a valid positive number.")

random_number = random.randint(0, top_of_range)
guesses = 0

print(f"\nGuess the number between 0 and {top_of_range}.")

while True:
    guesses += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Invalid input! Please type a valid number.")
        continue

    if user_guess < 0 or user_guess > top_of_range:
        print(f"Your guess is out of range! Please guess a number between 0 and {top_of_range}.")
        continue

    if user_guess == random_number:
        print(f"🎉 Congratulations! You guessed the number {random_number}!")
        break
    elif user_guess > random_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")

print(f"\nYou guessed the number in {guesses} tries.")
