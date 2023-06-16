
from Udemy_Projects.Hangman.Hangman_art import stages,logo
import random
print(logo)
word_list = ["ardwark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []
game_continues = True
life = 6
for x in chosen_word:
    display += "_"
while game_continues:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            display[letter] = guess
    print(display)
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        life -= 1
    print(stages[life])

    if "_" not in display:
        game_continues = False
        print("You won")
    elif life == 0:
        game_continues = False
        print("You lost")
        print("The word was: ",chosen_word)
