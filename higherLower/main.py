from art import logo, vs
from game_data import celebrities
import random

def correctGuess(celeb1, celeb2):
    return celeb1['followercount'] > celeb2['followercount']

print(logo)

def game():
    score = 0

    while True:
        celeb1, celeb2 = random.sample(celebrities, 2)

        print(f"\n{celeb1['name']}, {celeb1['description']} ({celeb1['country']})")
        print(vs)
        print(f"\n{celeb2['name']}, {celeb2['description']} ({celeb2['country']})")

        ans = input("\nWho has more followers? Enter 'higher' or 'lower': ")

        if ans == "higher":
            correct = correctGuess(celeb1, celeb2)
        elif ans == "lower":
            correct = correctGuess(celeb2, celeb1)
        else:
            print("\033[1;31;40mInvalid input. Please enter 'higher' or 'lower'.\033[m")
            continue

        if correct:
            score += 1
            print("\033[1;32;40mCorrect! You have a good eye for followers.\033[m")
            print(f"Your current score: {score}")
        else:
            print("\033[1;31;40mOops! Your guess wasn't correct this time.\033[m")
            print(f"Your final score: {score}")
            break

        print(f"{celeb1['name']} has {celeb1['followercount']} million followers.")
        print(f"{celeb2['name']} has {celeb2['followercount']} million followers.")

    return score

game()
while True:
    play_again = input("\nDo you want to play again? Enter 'yes' or 'no': ")
    if play_again.lower() != "yes":
        print("Thanks for playing!")
        break
    game()
