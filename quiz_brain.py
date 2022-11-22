import html


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        try:
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}: {q_text} "
        except IndexError:
            return "You have reached the end of the quiz"

    def check_answer(self,choice):
        correct_answer = self.current_question.answer
        if str(choice) == correct_answer:
            self.score += 1
            return True
        return False