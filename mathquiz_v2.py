import random

questions = 5
Incorrect_answer = 0
num_questions = 0
Correct_Answer = 0
game_history = []
mode = "regular"

# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code="xxx"):
    if low is None and high is None:
        error = "Please enter an integer"
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)
            elif high is not None and response > high:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

**** Instructions ****

To begin, choose the number of questions and try to get as many math questions you answer correct.

Then choose how many questions you'd like to answer. Press <enter> for infinite mode.

Your goal is to try to get as many math questions as possible right.

 Good luck.      

    ''')


print("➕➖ Welcome to the Math Quiz ✖️➗")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# FIX 1: Call instruction() if user wants instructions
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
# FIX 2: exit_code changed to "" so pressing enter triggers infinite mode
num_rounds = int_check("Questions (<enter> for infinite mode): ",
                       low=1, exit_code="")

# check for "" to turn on infinite mode
if num_rounds == "":
    mode = "infinite"
    num_rounds = 5

difficulty = input("Choose difficulty (easy, medium or hard): ").lower()

if difficulty == "easy":
    operations = ["+", "-"]
    low, high = 1, 10
elif difficulty == "medium":
    operations = ["+", "-", "*", "/"]
    low, high = 1, 20
else:
    operations = ["+", "-", "*", "/"]
    low, high = 10, 100


# Game loop starts here
while num_questions < num_rounds:
    # Rounds headings (based on mode)
    if mode == "infinite":
        rounds_heading = f"\n♾♾♾ Round {num_questions + 1} (Infinite Mode) ♾♾♾"
    else:
        rounds_heading = f"\n💿💿💿 Round {num_questions + 1} of {num_rounds} 💿💿💿"

    print(rounds_heading)

    random_operation = random.choice(operations)

    if random_operation == "/":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        question_num = num1 * num2
        answer = num1
    else:
        num1 = random.randint(low, high)
        num2 = random.randint(low, high)
        question_num = num1
        answer = eval(f"{num1} {random_operation} {num2}")

    if random_operation == "/":
        user_answer = int_check(f"What is {question_num} {random_operation} {num2}? ")
    else:
        user_answer = int_check(f"What is {num1} {random_operation} {num2}? ")

    # Check the answer
    if user_answer == answer:
        print("Correct!")
        Correct_Answer += 1
        feedback = "Correct"
    else:
        print(f"Wrong! The answer was {answer}")
        Incorrect_answer += 1
        feedback = "Wrong"

    # Save history each round
    if random_operation == "/":
        history_item = (f"Round {num_questions + 1}: {question_num} {random_operation} {num2} = "
                        f"{user_answer} (correct answer = {answer}, result = {feedback})")
    else:
        history_item = (f"Round {num_questions + 1}: {num1} {random_operation} {num2} = "
                        f"{user_answer} (correct answer = {answer}, result = {feedback})")

    game_history.append(history_item)

    num_questions += 1

    # if users are in infinite mode, increase number of rounds
    if mode == "infinite":
        num_rounds += 1
        num_rounds = 5

# Game loop ends here

# Statistics
if num_questions > 0:
    print(f"""
----Statistics----

Questions answered: {num_questions}
Correct answers: {Correct_Answer}
Wrong answers: {Incorrect_answer}
    """)

    # Ask if user wants game history and display it
    want_history = yes_no("Do you want to see the game history? ")
    if want_history == "yes":
        print()
        for item in game_history:
            print(item)