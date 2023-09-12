import random
from art import logo

print(logo)

def guessed():
    if level == "hard":
        chance = 5
    elif level == "easy":
        chance = 10
    
    while chance != 0:
        yourguess = int(input("Enter your guess: "))
        checkGuess(yourguess, guess)
        if yourguess == guess:
            return True
        chance -= 1
        print(f"Wrong answer.. You have {chance} chances left")
    
    return False
def checkGuess(myGuess, guess):
    if(myGuess>guess):
        print("Your guess is too high guess a short number")
    elif(myGuess<guess):
        print("Your guess is too low please guess a bigger number")
    
level = input("Please select your level: easy or hard\n")
guess = random.randint(0, 100)

if guessed():
    print("Congratulations! You guessed the correct number.")
else:
    print("Sorry, you didn't guess the correct number.")