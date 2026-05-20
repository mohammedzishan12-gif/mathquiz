import random

# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

**** Instructions ****

First choose how many rounds you want to do and the difficulty which goes from easy
medium or hard. Choose enter if you want infinite mode.
Type xxx if you want to quit

You will be asked a random math question each round. Try to get as many as 
you can correct.

 Good luck!   

    ''')

# checks for an integer with optional upper /
# lower limits and an optional exit code for infinite mode
# / quitting the game
def int_check(question, low=None, high=None, exit_code=None):
    # if any integer is allowed...
    if low is None and high is None:
        error = "Please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = (f"Please enter an integer that is "
                 f"more than / equal to {low}")

    # if the number needs to between low & high
    else:
        error = (f"Please enter an integer that"
                 f" is between {low} and {high} (inclusive)")

    while True:
        response = input(question).lower()

        # check for infinite mode / exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # Check the integer is not too low...
            if low is not None and response < low:
                print(error)

            # check response is more than the low number
            elif high is not None and response > high:
                print(error)

            # if the response is valid, return it
            else:
                return response

        except ValueError:
            print(error)

# Variables
score = 0
questions = 5

game_history = []
all_scores = []

print("✖️➕➖➗ Math Quiz ➗➖➕✖️")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

# Ask user for number of rounds / infinite mode
num_rounds = int_check("Rounds <enter for infinite>: ",
                       low=1, exit_code="xxx")

if num_rounds == "":
    mode = "infinite"
    num_rounds = 5



difficulty = input("Choose difficulty (easy, medium or hard): ").lower()

# Set operations and number range based on difficulty
if difficulty == "easy":
    operations = ["+", "-"]
    min, max = 1, 10
elif difficulty == "medium":
    operations = ["+", "-", "*", "/"]
    min, max = 1, 20
else:
    operations = ["+", "-", "*", "/"]
    min, max = 10, 100

# game loop start
while True:
    random_operation = random.choice(operations)

    # Generate numbers
    if random_operation == "/":
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        question_num = num1 * num2
        answer = num1
    else:
        num1 = random.randint(min, max)
        num2 = random.randint(min, max)
        question_num = num1
        answer = eval(f"{num1} {random_operation} {num2}")

    # Show the questiona
    if random_operation == "/":
        user_answer = int(input(f"\nWhat is {question_num} {random_operation} {num2}? "))
    else:
        user_answer = int(input(f"\nWhat is {num1} {random_operation} {num2}? "))

    # Check the answer
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The answer was {answer}")

        # if user has entered exit code, end game!!
        if end_game == "yes":
            break

        rounds_played += 1

        # Add round result to game history
        history_feedback = f"Round {rounds_played}: {feedback}"
        game_history.append(history_feedback)

        # add guesses used to score list
        all_scores.append(guesses_used)

        # if users are in infinite mode, increase number of rounds!
        if mode == "infinite":
            num_rounds += 1

# Game loop ends here

# check users have played at least one round
# before calculating statistics.
if rounds_played > 0:
    # Game History / Statistics area

    # Calculate statistics
    all_scores.sort()
    best_score = all_scores[0]
    worst_score = all_scores[-1]
    average_score = sum(all_scores) / len(all_scores)

    # Output the statistics
    print("\n📊📊📊 Statistics 📊📊📊")
    print(f"Best:{best_score} | Worst:{worst_score} | Average:{average_score:.2f} ")
    print()

    # Display the game history on request
    see_history = yes_no("Do you want to see your game history? ")
    if see_history == "yes":
        for item in game_history:
            print(item)

# if users have quit without playing a round, end the program gracefully.
else:
    print("🐔🐔🐔 Oops - you chickened out and did not play any rounds. 🐔🐔🐔")




