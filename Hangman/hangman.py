import random
import time


def main():
    name = str(input("Enter your name: ")).title()
    print(f"Hi, {name}. This is Hangman. Rules are simple: \n1. You have 5 chances to guess the word")

    attempts = 3
    words_list = ['word', 'hangman', 'python', 'activities']
    chosen_word = random.choice(words_list)
    chosen_word_list = list(chosen_word)
    stock_letters = []
    word = list("_" * len(chosen_word))

    time.sleep(0.4)
    print(f"\nWe choose: {word} \nNow you can start :)")
    while True:
        player = input("\nGuess a letter: ").lower()
        correct = 0

        for letter in chosen_word_list:
            if player == letter:
                ind = chosen_word_list.index(letter)
                stock_letters.append(player)
                chosen_word_list[ind] = 0
                word[ind] = letter
                correct = 1

        if word == list(chosen_word):
            print(f"\n{name}, you won! The choosen word was {chosen_word}.")
            break

        if correct == 0:
            attempts -= 1
            print(f"\nAttempts remaining: {attempts}")

        if attempts == 0:
            print(f"\n{name}, you lose!")
            break

        print(word)


if __name__ == '__main__':
    main()
