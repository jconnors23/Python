from question_model import Question
from data import question_data  # convert question data to question objects that will be usable
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    new_question = Question(entry['question'], entry['correct_answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_questions():
    quiz.next_question()
print(quiz.final_score())
