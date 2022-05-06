class QuizBrain:

    def __init__(self, g_list):
        self.question_number = 0       # номер вопроса
        self.score = 0
        self.question_list = g_list       # список всех вопросов объектов

    def still_has_questions(self):
        """ пока есть вопросы возвращает правду"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """задаёт вопросы и принимает ответы"""
        current_question = self.question_list[self.question_number]    # question_bank[question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        """проверяет правильность ответов"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

    def final_answer(self):
        print("You have completed the Quiz")
        print(f"You final score was: {self.score}/{self.question_number}")