import question_model
from data import question_data
from quiz_brain import  QuizBrain


def create_question_bank():
    question_bank = []
    for q in question_data:
        question = question_model.Question(q["text"], q["answer"])
        question_bank.append(question)
    return question_bank


quiz = QuizBrain(create_question_bank())

while quiz.still_next_question():
    quiz.next_question()
    print(f"Your score is {quiz.score}.\n")

