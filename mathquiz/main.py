import random

score = 0
questions = 5

name = input("Enter your name: ")
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

for i in range(questions):
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

# Final score
print(f"\n{name}, you scored {score} out of {questions}!")

