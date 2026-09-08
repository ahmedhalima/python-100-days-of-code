from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

questionBank = []
for question in question_data:
    questionBank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(questionBank)
while quiz.still_has_questions():
    quiz.next_question()