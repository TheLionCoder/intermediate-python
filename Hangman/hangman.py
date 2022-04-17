import random
import os
from hangman_art import stages, logo
    

def read_data():
    word_list = []
    with open("data.txt", "r", encoding="utf_8") as file:
        for word in file:
            word_list.append(word.strip().lower())
    return word_list


def main():
    
    print(logo)
    LIVES = 6

    end_of_game = False
    data = read_data()
    chosen_word = random.choice(data)
    word_length = len(chosen_word)
    print("{} {}.".format(chosen_word, word_length))

    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:

        guess = input("Guess a letter: ").lower()
        assert guess.isalpha() and len(guess)==1 , "Please only Letters and only one."
        os.system("clear")
        
        if guess in display:
            print("Ey {} letter has been guessed before, try another one".format(guess))
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if guess not in chosen_word:
            LIVES -= 1
            print("{} LIVES remain, you guessed {} letter, that's not in the word 💀.".format(LIVES, guess))
            if LIVES == 0:
                end_of_game = True
                print("You lose.")

        print("{}".format(' '.join(display)))

        if "_" not in display:
            end_of_game = True
            print("You win.")

        print(stages[LIVES])


if __name__ == '__main__':
    main()