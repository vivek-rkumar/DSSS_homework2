import random
def generating_random_integer(minimum, maximum):
    """
    Generate a random integer between the specified minimum and maximum values.
    Parameters:
    - minimum (int): The minimum value for the random integer.
    - maximum (int): The maximum value for the random integer.
    Returns:
    - int: A random integer between minimum and maximum (inclusive).
    """
    return random.randint(minimum, maximum)
def generating_random_operation():
    """
    Select a random arithmetic operation from the set {+, -, *}.
    Returns:
    - str: A randomly chosen arithmetic operation.
    """
    return random.choice(['+', '-', '*'])
def generating_question_and_answer(number1, number2, operation):
    """
    Generate a math question and calculate the correct answer.
    Parameters:
    - number1 (int): The first operand of the arithmetic operation.
    - number2 (int): The second operand of the arithmetic operation.
    - operation (str): The arithmetic operation {+, -, *}.
    Returns:
    - tuple: A tuple containing the generated question (string) and the correct answer (int).
    """
    question = f"{number1} {operation} {number2}"
    if operation == '+':
        answer = number1 + number2
    elif operation == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2
    return question, answer


def math_quiz():
    """
    Run a simple math quiz game.
    The user is presented with math problems and must provide correct answers to earn points.
    """
    your_score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        number1 = generating_random_integer(1, 10)
        number2 = generating_random_integer(1, 5)
        operation = generating_random_operation()
        problem, solution = generating_question_and_answer(number1, number2, operation)
        print(f"\nQuestion: {problem}")

        while True:
            user_answer = input("Your answer: ")
            try:
                user_answer = int(user_answer)
                break
            except ValueError:
                print("Invalid input. Please enter an integer and try again")

        if user_answer == solution:
            print("Correct! You earned a point.")
            your_score += 1
        else:
            print(f"Wrong answer. The correct answer is {solution}.")

    print(f"\nGame over! Your score is: {your_score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
