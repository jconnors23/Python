class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        item = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {item.text} True | False?\n")
        self.check_answer(user_answer, item.answer)

    def still_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.score += 1
            print('correct')
        else:
            print('incorrect')
        print(f'answer was {correct_answer}\n')
        print(f'current score is {self.score}/{self.question_number}\n')

    def final_score(self):
        return (f"Final score of {self.score}/{self.question_number}")