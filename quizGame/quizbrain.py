class QuizBrain:
    def __init__(self, question_list):
        self.question_number = -1  
        self.questions = question_list
        
    def next_question(self):
        continue_quiz = True
        score=0
        while continue_quiz:
            
            self.question_number += 1
            
            if self.question_number >= len(self.questions):
                print("End of the quiz.")
                break
            
            user_answer = input(f"Question {self.question_number + 1}: {self.questions[self.question_number].text} (True/False)\n")
            correct_answer = self.questions[self.question_number].answer
            
            if user_answer.lower() == correct_answer.lower():
                score+=1
                print(f"Your answer is correct! \n and your score is {score}")
                
            else:
                print(f"You got it wrong. The correct answer is {correct_answer}.")            