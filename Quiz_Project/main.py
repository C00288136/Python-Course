from question_model import question
from data import question_data
from quiz_brain import Quizbrain
question_bank = []
for item in question_data:
    # here remember that the "item" is the current instance in the dictionary so the whole section containing the
    # answer and the question
    question_text = item["question"]
    question_answer = item["correct_answer"]
    new_question = question(question_text,question_answer)
    question_bank.append(new_question)
    
quiz = Quizbrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    
print("You completed the quiz")
print(f"Your final score was {quiz.score}/{len(quiz.question_list)}")
