class quiz_brain:
    def __init__(self, question_list):
        self.question_number=0
        self.question_list=question_list
        
    def next_question(self):
        input(f"Q.{self.question_number()+1} is {self.question_list[self.quiz_number]} True/False \n")
        
        
        
