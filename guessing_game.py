#this is a guess the number game
import random
print("Hello, what is your name?")
name = input()
print("Hi " + name + "!", "I'm thinking of a number between 1 and 20.")
secret_number = random.randint(1,20)

#This will allow X number of guesses
for guesses_taken in range (1,7):
    print("Take a guess")
    guess = int(input())
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        break # this will trigger if they guessed correctly

if guess == secret_number:
    print("Good Job " + name +"!" +" It took you " + str(guesses_taken) + " guesses!" )
else:
    print("Nope. The number I was thinking of was " + str(secret_number))
