from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    
        
    def __init__(self,quiz_brain: QuizBrain) :
        self.quiz = quiz_brain
        # create the window/frame
        self.window = Tk()
        # sets the title (can also be done in the widow settings or config)
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        
        # make a score label in the top of the page
        self.score_label = Label(text="Score: 0", foreground="white",background=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        
        # canvas used for the text like a Jpanel
        self.canvas = Canvas(width=300,height=250,bg="white")
        # Works like a JLabel where we will in the field with text
        self.question_text = self.canvas.create_text(150,125, 
                                                     text="Some Question Text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial",20,"italic"),
                                                     width=280)
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)
        # Photo image used to read a image from a file
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image,highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2,column=0)
        self.false_button = Button(image=false_image, highlightthickness=0,command=self.check_false)
        self.false_button.grid(row=2,column=1)
        
        self.get_nextQ()
        
        # mainloop works same as setvisible in java to show and run the code
        self.window.mainloop()
        
        
    def get_nextQ(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions(): 
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!!")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        print("check true ran")

    
    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))
        print("check false ran")
    
    def give_feedback(self,is_right):
        if is_right :
            self.canvas.config(bg="green")
            
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_nextQ)
        

        
