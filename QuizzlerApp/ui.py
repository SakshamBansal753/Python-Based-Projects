THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz:QuizBrain):
        self.quiz=quiz
        self.windows=Tk()
        self.windows.minsize(height=500,width=600)
        self.windows.config(padx=20,pady=20)
        self.windows.title("Quiz")
        self.windows.config(bg=THEME_COLOR)
        self.score_label=Label(text="Score:0",bg=THEME_COLOR,fg="white",pady=20,font=("Arial",20,"bold"))
        self.score_label.grid(column=1,row=0)
        self.canvas=Canvas(height=280,width=300,bg="white",highlightthickness=0)
        self.q_t=self.canvas.create_text(150,125,width=250,text="Hello Tkinter",font=("Arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=20,padx=20)
        self.ia=PhotoImage(file="images/false.png")
        self.button1=Button(image=self.ia,highlightthickness=0,pady=20,bg=THEME_COLOR,command=self.false_p)
        self.button1.grid(column=1,row=2)
        self.ib=PhotoImage(file="images/true.png")
        self.btn2=Button(image=self.ib,highlightthickness=0,pady=20,bg=THEME_COLOR,command=self.true_p)
        self.btn2.grid(column=0, row=2)
        self.get_next()
        self.windows.mainloop()


    def get_next(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score:{self.quiz.score}")
            question=self.quiz.next_question()
            self.canvas.itemconfig(self.q_t,text=question)
        else:
            self.canvas.itemconfig(self.q_t,text="Quiz has ended")
            self.btn2.config(state="disabled")
            self.button1.config(state="disabled")
    def true_p(self):

        self.feedback(self.quiz.check_answer("True"))
    def false_p(self):
        is_check=self.quiz.check_answer("False")
        self.feedback(is_check)
    def feedback(self,is_ok):
        if is_ok:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.windows.after(1000,self.get_next)




