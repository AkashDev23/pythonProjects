import random
from logo import logo
from words import word_list
from logo import hangman_stages

print (logo)

chosenWord = random.choice(word_list)
wordInList = list(chosenWord)

str=" "
print ("Hint: It's a type of food.")
display = ["_" for _ in chosenWord]

lives=0
max_lives=7
while display != wordInList and lives < max_lives:
    guess = input("Guess a letter\n").lower()
    

    guessed_correctly = False 

    for index in range(len(chosenWord)):
        if guess == chosenWord[index]:
            display[index] = guess
            guessed_correctly = True 
    
    if not guessed_correctly:
        print(hangman_stages[lives])
        lives+=1
    print(str.join(display))


if lives >= max_lives:
    print("The correct word was "+chosenWord)
    print("You've run out of lives. Game over.")
else:
    print("Congratulations! You won the game.")

