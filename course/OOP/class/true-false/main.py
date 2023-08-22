from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []

for question  in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print(f"You have completed the quiz, Your final score was: {quiz.score}/{quiz.question_number}")
        