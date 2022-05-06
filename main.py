from question_model import Quesstion
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:      # перебираем каждый вопрос в question_data
    question_text = question["text"]     # вопросы  ключ
    question_answer = question["answer"]      # ответы  ключ
    new_question = Quesstion(question_text, question_answer)
    question_bank.append(new_question)      # получили 12 объектов в каждом сохраняется вопрос и ответ

quiz = QuizBrain(question_bank)    # атрибут банк списков

while quiz.still_has_questions():
    quiz.next_question()

quiz.final_answer()
print("You have completed the Quiz")
print(f"You final score was: {quiz.score}/{quiz.question_number}")
