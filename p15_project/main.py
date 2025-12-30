# Project 15 - Quiz

# Include imports
from art import logo
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Class & Function definitions
def generate_question_bank():
    """
    Generate a bank of questions.
    :return: List of all questions.
    :rtype: list
    """
    questions = []
    for question in question_data:
        current_q = Question(question["text"], question["answer"])
        questions.append(current_q)
    return questions

# Output logo
print(logo)

# Initial greeting
print("Welcome to the True or False Quiz!")

# Main Logic
question_bank = generate_question_bank()
quiz = QuizBrain(question_bank)

print("Let's see how many you can get right!")
while quiz.still_has_questions():
    answer = quiz.next_question()
    print(f"Current score: {quiz.score}/{quiz.question_number}!\n")

print(f"You have a total of {quiz.score}/{len(question_bank)}!")
