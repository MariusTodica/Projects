import time


def quiz():
    active = True
    print("Hello to the quiz app. It is simple how it sound.")
    name = input("Enter your name to get started: ").title()
    ready = input(f"Are you ready, {name}?[y/n]: ")

    if ready == 'n':
        print("OK..")
        exit()
    elif ready == 'y':
        return active
    else:
        quiz()


def game():
    questions_math = ("1. What is 1 + 1", "2. What is 2 + 2",)
    answers_math = (2, 4)

    questions_geo = ("Romanian Capital", "Belgia Capital")
    answers_geo = ("Bucharest", "Bruxeless")

    total_questions = len(questions_math + questions_geo)

    var_result = "Answer: "
    correct = "Correct!"
    fals = "Incorrect! The answer is"

    score = 0

    for questions_math, answers_math in zip(questions_math, answers_math):
        time.sleep(1)
        print(questions_math)
        result = int(input(var_result))
        if result != answers_math:
            print(fals, answers_math)
        else:
            print(correct)
            score += 1

    for questions_geo, answers_geo in zip(questions_geo, answers_geo):
        time.sleep(1)
        print(questions_geo)
        result = str(input(var_result)).title()
        if result != answers_geo:
            print(fals, answers_geo)
        else:
            print(correct)
            score += 1

    percentage = (score / total_questions) * 100

    print("Quiz completed!")
    print("Score:", score, "/", total_questions)
    print("Percentage:", percentage, "%")

    if percentage > 49.9:
        print("You passed.")
    else:
        print("You failed.")


if __name__ == '__main__':
    quiz()
    game()
