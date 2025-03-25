class QuizBrain:
    def __init__(self,question_list):
             self.question_number=0
             self.question_list=question_list
             self.score=0
    def still(self):
        if self.question_number<len(self.question_list):
           return True
        else:
            return False

    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number += 1
        user_answer=     input(f"Q {self.question_number}:{current_question.text}   🚨 Type True ✅ Or False ❌ ------->")
        self.check_answer(user_answer,current_question.answer)
    def check_answer(self,user_answer,answer):
        if user_answer.lower()==answer.lower():
            self.score+=1
            print(f"You Are Correct ,correct answer is \n✅{answer}")
        else:
            print(f"You are wrong ❌ , correct answer is\n{answer}")
    def display(self):
        print(f"Your Current Score is {self.score}/{self.question_number}\n")






