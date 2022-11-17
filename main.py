from question_model import Question
from data import question_data
from ui import QuizInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz_ui = QuizInterface(question_bank)
while quiz_ui.quiz_brain.still_has_questions():
    quiz_ui.quiz_brain.next_question()
