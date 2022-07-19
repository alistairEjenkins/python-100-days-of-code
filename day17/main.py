from question_model import Question
from data import question_data
from quiz_brain import Quizbrain
from os import system
import time

question_bank = [Question(question['question'], question['correct_answer']) for question in question_data]

quizbrain = Quizbrain(question_bank)

while quizbrain.still_has_questions():
    system('cls')
    quizbrain.next_question()
    time.sleep(4)

print("Youveciompleted the quiz!")
print(f"Your final score: {quizbrain.score}/{len(quizbrain.question_list)}")