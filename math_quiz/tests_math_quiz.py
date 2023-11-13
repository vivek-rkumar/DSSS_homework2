import unittest
from math_quiz import generating_random_integer, generating_random_operation, generating_question_and_answer

class TestMathGame(unittest.TestCase):

    def test_generating_random_integer(self):
        """
        Test if random numbers generated are within the specified range.
        """
        min_val = 1
        max_val = 20
        for _ in range(500):  # Generate a large number of random values
            rand_num = generating_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generating_random_operation(self):
        """
        Test the generation of random arithmetic operations.
        """
        for _ in range(500):  # Generate a large number of random operations
            operation = generating_random_operation()
            self.assertIn(operation, ['+', '-', '*'])

    def test_generating_question_and_answer(self):
        """
        Test the generation of math problems and correct answers.
        """
        test_cases = [
            (12, 4, '+', '12 + 4', 16),
            (9, 3, '-', '9 - 3', 6),
            (2, 8, '*', '2 * 8', 16),
            (15, 3, '+', '15 + 3', 18),
            (6, 2, '-', '6 - 2', 4),
            (4, 2, '*', '4 * 2', 8),
            (2, 1, '+', '2 + 1', 3),
            (10, 5, '-', '10 - 5', 5),
            (7, 2, '*', '7 * 2', 14),
            (3, 2, '+', '3 + 2', 5),
        ]

        for number1, number2, operator, expected_problem, expected_answer in test_cases:
            # Generate a math problem and correct answer
            problem, answer = generating_question_and_answer(number1, number2, operator)
            
            # Check if the generated problem matches the expected problem
            self.assertEqual(problem, expected_problem)
            
            # Check if the generated answer matches the expected answer
            self.assertEqual(answer, expected_answer)

if __name__ == "__main__":
    unittest.main()
