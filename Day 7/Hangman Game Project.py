#Hangman Project

import random
import hangaman_art
from hangman_wordlist import word_list

print("Welcome to the Hangman Game!")
print(hangaman_art.logo)

display = []
lives = 6 
chosen_word = random.choice(word_list)

for i in chosen_word:
    display += "_"
print (f"The chosen word is: {display}")


end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guesses {guess}")


    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life! ")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"You lose! Game over. The word was {chosen_word}") 
        
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You have won")
    from hangaman_art import stages
    print(stages[lives])