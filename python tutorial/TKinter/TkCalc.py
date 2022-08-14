from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10,pady=10)


def button_click(number):
  current = e.get()
  e.delete(0, END)
  e.insert(0, str(current) + str(number))

def on_clear():
  e.delete(0, END)
  
def on_addition():
  global firstNum
  firstNum = int(e.get())
  e.delete(0, END)

def on_subtract():
  firstNum = int(e.get())
  e.delete(0, END)

def on_multiply():
  firstNum = int(e.get())
  e.delete(0, END)

def on_divide():
  firstNum = int(e.get())
  e.delete(0, END)

def on_equals():
  secondNum = int(e.get())
  e.delete(0, END)
  e.insert(0, firstNum + secondNum)
  
  

#make buttons padx for each row should = 120, or 119 with special chars. 
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_addition = Button(root, text="+", padx=39, pady=20, command=on_addition)
button_subtract = Button(root, text="-", padx=40, pady=20, command=on_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=on_multiply)
button_divide = Button(root, text="/", padx=40, pady=20, command=on_divide)
button_equals = Button(root, text="=", padx=87, pady=20, command=lambda: on_equals())
button_clear = Button(root, text="Clear", padx=80, pady=20, command=on_clear)

#align buttons
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)
button_0.grid(row=4,column=1)
#handle operator rows

button_addition.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)
button_multiply.grid(row=3,column=3)
button_divide.grid(row=4,column=3)
button_equals.grid(row=6,column=2,columnspan=2)
button_clear.grid(row=6,column=0, columnspan=2)


root.mainloop()
