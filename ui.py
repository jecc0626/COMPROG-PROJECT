from tkinter import *  

class CalculatorGUI:

    window = ""
    equation_string = ""
    result = ""
    
    def __init__(self):
        pass
    def SetOnEqualHandler(self, event):
        self.OnEqualHander = event;
        print("Handler Set")
    def initializeGUI(self, calculator):
        
        window = Tk()

        window.title('Calculator')

        window.geometry('355x475')

        window.configure(background='#ff99bb')

        window.resizable(width=False,height=False)


        def press(num):
            self.equation_string = self.equation_string + str(num)
            equation.set(self.equation_string)
                
        def equalpress():
            result = calculator.Evaluate(self.equation_string)
            if(result != "Error"):
                self.equation_string = str(result)
                equation.set(result)
            else:
                equation.set("Error")
            
        def clear():
                result = ''
                self.equation_string = ""
                equation.set('0')

        def backspace():
            self.equation_string = self.equation_string[:-1]
            equation.set(self.equation_string)

        button_frame = Frame(window,background='#ff99bb')
        button_frame.pack()
        
        equation = StringVar()
        
        expression_field = Entry(button_frame, state="readonly", textvariable=equation,justify='right',font=('arial',20,'bold'))

        button1 = Button(button_frame,text='1',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(1))

        button2 = Button(button_frame,text='2',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(2))

        button3 = Button(button_frame,text='3',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(3))

        addition = Button(button_frame,text='+',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press('+'))

        button4 = Button(button_frame,text='4',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(4))

        button5 = Button(button_frame,text='5',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(5))

        button6 = Button(button_frame,text='6',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(6))

        subtraction = Button(button_frame,text='-',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press('-'))

        button7 = Button(button_frame,text='7',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(7))

        button8 = Button(button_frame,text='8',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(8))

        button9 = Button(button_frame,text='9',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(9))

        multiplication = Button(button_frame,text='*',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press('*'))

        button1 = Button(button_frame,text='1',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(1))

        button0 = Button(button_frame,text='0',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press(0))

        decimal = Button(button_frame,text='.',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press('.'))

        clear = Button(button_frame,text='C',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=clear)

        division = Button(button_frame,text='/',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=lambda:press('/'))

        equal = Button(button_frame,text='=',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=equalpress) 

        expression_field.grid(row=0,column=0,columnspan=4,ipadx=8,ipady=25,pady=15)

        clear.grid(row=1,column=0,columnspan=3)
        division.grid(row=1, column=3)

        button7.grid(row=2,column=0)
        button8.grid(row=2,column=1)
        button9.grid(row=2,column=2)
        multiplication.grid(row=2,column=3)

        button4.grid(row=3,column=0)
        button5.grid(row=3,column=1)
        button6.grid(row=3,column=2)
        subtraction.grid(row=3,column=3)

        button1.grid(row=4,column=0)
        button2.grid(row=4,column=1)
        button3.grid(row=4,column=2)
        addition.grid(row=4,column=3)

        button0.grid(row=5,column=0,columnspan=2)
        decimal.grid(row=5,column=2)
        equal.grid(row=5,column=3)

        backspace = Button(button_frame,text='DEL',font=('times new roman',12),relief='ridge',bd=1,bg='#ffe6ee',width=8,height=3,command=backspace)
        backspace.grid(row=1, column=2)


        window.mainloop()