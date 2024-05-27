class Quizbrain:
    def __init__(self, q_list) -> None:
        # remember to use self the talk about the object inself in the methods aswell as attributes
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        curreent_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curreent_question.text} (True/False)")
        self.check_answer(user_answer, curreent_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct):
        if answer.lower() == correct.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Thats wrong")
        print(f"The correct answer is {correct}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")
