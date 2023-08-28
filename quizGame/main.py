from question_model import Question
from data import question_data

question_bank=[]
for question in question_data:
    new_question=question["text"]
    new_answer=question["answer"]
    

print(new_answer)