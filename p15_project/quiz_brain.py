# Constant and global definitions
ANWERS=("True", "False", "true", "false")


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def prompt_answer(self, current_question):
        return input(f"Q.{self.question_number}: {current_question.text} - (True/False)?\n")
    
    def check_answer(self, answer, current_answer):
        return answer.lower() == current_answer.lower()
    
    def save_answer(self, answer, current_question):
        self.score += 1 if self.check_answer(answer=answer, current_answer=current_question.answer) else 0
    
    def still_has_questions(self):
        return not self.question_number == len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = self.prompt_answer(current_question)
        print(f"Correct answer is: {current_question.answer}!")
        
        if answer not in ANWERS:
            print("Invalid input provided! Please, type True/False.")
            self.prompt_answer(current_question)
        else:
            self.save_answer(answer, current_question)

        return answer
