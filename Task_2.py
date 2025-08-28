import random

the_randomNum = random.randint(1, 100)
guess = 0
while guess < 10:
    user_guess = input("Please enter your guess (1-100): ")
    try:
        user_guess = int(user_guess)
        guess += 1
        if user_guess == the_randomNum:
            print("You guessed the random number correctly!" + " "+ "Attempts used: " + str(guess) + " " + "of 10")
            break
        elif user_guess > the_randomNum:
            print("Too high! Try again." + " " + "Your guess attempt: " + str(guess) + " " + "of 10")
        elif user_guess < the_randomNum:
            print("Too low! Try again." + " " + "Your guess attempt: " + str(guess) + " " + "of 10")
    except ValueError:
        print("Letters are not allowed. Use numbers for your guess.")
    
else:
    print("Game Over! You have reached the maximum number of guesses. The random number was: " + str(the_randomNum))
    