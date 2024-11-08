import random

def guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game! Try to guess the number between 1 and 100!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 69
            
            if guess < secret_number:
                print("The number is higher!")
            elif guess > secret_number:
                print("The number is lower!")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer!")

guessing_game()

## There is an easter egg in this code :)
