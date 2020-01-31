from tkinter import *

class BMI:

    def __init__(self):
        window = Tk()
        window.title("BMI CALCULATOR")
        frame1 = Frame(window)
        frame1.pack()
        
        self.height = DoubleVar()
        h_label = Label(frame1, text = "Height", fg ="blue")
        self.heigh = Entry(frame1, textvariable= self.height)
        h_label.grid(row = 2)
        self.heigh.grid(row = 3, column = 1)

        self.mass = DoubleVar()
        w_label = Label(frame1, text = "Mass", fg ="blue")
        self.mas = Entry(frame1, textvariable = self.mass)
        w_label.grid(row = 4)
        self.mas.grid(row = 5, column = 1)

        self.bmi_Val = DoubleVar()
        self.stat = StringVar()
        bmi = Label(frame1, text = "BMI:", fg ="blue", justify = LEFT)
        status = Label(frame1, text = "Status: ", fg ="blue")
        status_msg = Label(frame1, textvariable = self.stat, fg = "Blue")
        BMI_total =  Label(frame1, textvariable = self.bmi_Val, fg = "Blue")
        bmi.grid(row =6)
        status.grid(row = 7)
        BMI_total.grid(row =6, column = 1)
        status_msg.grid(row = 7, column = 1)

        calculate = Button(frame1, text="Calculate", command=self.calc,  bg = "blue")
        clear = Button(frame1, text="Reset", bg = "red", command=self.clear)
        calculate.grid(row = 8)
        clear.grid(row = 8, column =3)
        window.mainloop()
        
    def calc(self):
        BMI = self.BMI_val(self.mass.get(), self.height.get())
        Stat = self.getStatus()
        self.stat.set(Stat)
        self.bmi_Val.set(format(BMI, ".2f"))
        
    
    def BMI_val(self, mass, height):
        return mass / height ** 2
    
    def getHeight(self):
        return self.height
    
    def clear(self):
        self.stat.set('')
        self.bmi_Val.set('0.0')
        self.mas.delete(0, 'end')
        self.heigh.delete(0, 'end')
    
    def getWidth(self):
        return self.mass
        
    def getStatus(self):
        if self.bmi_Val.get() > 40:
            return "You are Obess Class 3"
        elif self.bmi_Val.get() > 35 or self.bmi_Val.get() < 40:
            return "You are Obess Class 2"
        elif self.bmi_Val.get() > 30 or self.bmi_Val.get() < 35:
            return "You are Obess Class 1"
        elif self.bmi_Val.get() > 25 or self.bmi_Val.get() < 30:
            return "You are Overweight"
        elif self.bmi_Val.get() > 18.5 or self.bmi_Val.get() < 25: 
            return "You are Normal"
        elif self.bmi_Val.get() > 17 or self.bmi_Val.get() < 18.5:
             return "You are Mild Thin"
        else:
            return "You are Moderately Thin"

BMI()
