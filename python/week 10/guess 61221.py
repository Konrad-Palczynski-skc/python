# A program to demonstrate the single if statement
import random

number = random.randint (1, 10)
 #print(number)

guess = int(input("Enter a number between 1 and 10: "))

# Evaluate the condition
if guess == number:
    print(number)
    print("Your guess was correct")
    print("Well done!")
else:
    if guess != number:
        print("The number was", number)
print("Your guess was incorrect")