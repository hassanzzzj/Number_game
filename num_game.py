import random


print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
    
   
secret_number = random.randint(1, 100)
attempts = 0
guessed = False

while not guessed:
        try:
            # Prompt the user for their guess
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            
            # Check if the guess is within the valid range
            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue
            
            # Compare the guess to the secret number
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
        
        except ValueError:
            print("Invalid input! Please enter a number.")
