import random

global player


def description():

    message = input(f"Hi! Welcome to guessing the number. \nYou have to choose a number between 0-10. \nReady?[y/n]: ")

    if message == 'n':
        print("OK..")
        exit()
    elif message == 'y':
        return True
    else:
        description()


def number():
    global player
    robot = random.randint(0, 10)
    attempt = 0

    while True:
        try:
            player = int(input("Choose a number[0-10]: "))

        except ValueError:
            print("Enter a number")

        if player < 0 or player > 10:
            print("Choose a number between 0 and 10: ")

        if player == robot:
            print("You guessed the number.")
            break

        if player != robot and attempt < 3:
            attempt += 1
            print(f"Incorrect, attempts remaining: {3 - attempt}")
        else:
            print(f"\nIncorrect, the correct number is: {robot}")
            break

    try_again()


def try_again():
    again = str(input("You want to try again?[y/n]: "))
    if again == 'n':
        print("OK..")
        exit()
    elif again == 'y':
        number()
    else:
        try_again()


if __name__ == '__main__':
    description()
    number()
