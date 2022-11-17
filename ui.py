from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:
    def __init__(self, questions):
        # WINDOW SETTINGS
        self.window = Tk()
        self.quiz_brain = QuizBrain(questions)
        self.window.title("Trivia Game")
        self.window.config(padx=20, pady=20, bg="#375362")
        # SCORE LABEL SETTINGS
        self.score = Label(
            text=f"Score: {self.quiz_brain.score}", fg="white", bg="#375362")
        self.score.grid(row=0, column=1)
        # CANVAS SETTINGS
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question = self.quiz_brain.next_question()
        self.question_text = self.canvas.create_text(
            150, 125, text=self.question, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        # BUTTON SETTINGS
        self.false_img = PhotoImage(file="images/false.png")
        self.true_img = PhotoImage(file="images/true.png")
        self.false_button = Button(image=self.false_img, highlightthickness=0)
        self.false_button.grid(row=2, column=0)
        self.true_button = Button(image=self.true_img, highlightthickness=0)
        self.true_button.grid(row=2, column=1)
        self.window.mainloop()
