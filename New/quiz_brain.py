class QuizBrain:
    def __init__(self, question_list, question_number=0):
        self.question_list = question_list
        self.question_number = question_number
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {question.text} (True or False)?: ")
        self.check_answer(user_answer, question.answer)

    def still_next_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
            self.question_number = len(self.question_list)
        print(f"The correct answer is : {correct_answer}.")

