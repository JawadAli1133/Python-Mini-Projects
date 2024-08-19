from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = 'Quizler'
        self.window.config(pady=20,
                           padx=20,
                           background=THEME_COLOR)
        self.score_label = Label(text=f'Score: 0',
                                 fg='white',
                                 bg=THEME_COLOR)
        self.score_label.grid(row=0,
                              column=1)

        self.canvas = Canvas(width=400,
                             height=400,
                             bg="white",
                             highlightthickness=0)
        self.question_text = ''
        self.set_canvas()
        self.get_next_question()
        wrong_image = PhotoImage(file='images/false.png')
        right_image = PhotoImage(file='images/true.png')
        self.wrong_button = Button(image=wrong_image, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=0)
        self.right_button = Button(image=right_image, command=self.true_pressed)
        self.right_button.grid(row=2, column=1)
        self.window.mainloop()

    def set_canvas(self):
        self.question_text = self.canvas.create_text(200,
                                                     200,
                                                     width=380,
                                                     text='Question will be displayed here',
                                                     font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

    def get_next_question(self):
        question = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=question)

    def change_canvas_color(self):
        self.canvas.config(background='white')

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.score_label.config(text=f'Score: {self.quiz.score}')
        self.window.after(500, self.change_canvas_color)
        self.get_next_question()
