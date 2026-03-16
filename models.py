from datetime import datetime

class Question:
    def __init__(self, q_id, text, options, correct_answer):
        self.q_id = q_id
        self.text = text
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        if not user_answer:
            return False
        return str(user_answer).strip().upper() == self.correct_answer.upper()

def get_sample_questions():
    return [
        Question(1, "What does OOP stand for?", ["A) Object Oriented Programming", "B) Object Only Process", "C) Oriented Python", "D) None"], "A"),
        Question(2, "Which data structure follows LIFO?", ["A) Queue", "B) Stack", "C) List", "D) Dictionary"], "B"),
        Question(3, "Flask is primarily used for building:", ["A) Desktop apps", "B) Web applications", "C) Mobile games", "D) Databases"], "B"),
        Question(4, "In a Queue we follow:", ["A) LIFO", "B) FIFO", "C) Random", "D) FILO"], "B"),
        Question(5, "What does the __init__ method do?", ["A) Deletes object", "B) Initializes object", "C) Prints class", "D) None"], "B"),
        Question(6, "Correct way to import datetime?", ["A) import datetime", "B) from datetime import datetime", "C) Both A and B work", "D) import time"], "C"),
    ]