# Guess Game - 3 guesses
import random

number = random.randint(1, 10)
#print(number)

# Initialise a loop counter
counter = 0

# Loop 3 times
while counter <= 3:
    
    guess = int(input("Enter a number between 1 and 10: "))
    if guess == number:
        print("Correct")
        break
    elif guess < number:
        print("Too low")
    else:
            print("Too high")
            
            counter = counter + 1
            
            print("Hard luck")
            
