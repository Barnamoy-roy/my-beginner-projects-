#building basic calculator
#note that this calculator only adds numbers i will improve it later in the future when i get more knowledge about tkinter

#import tkinter

from tkinter import *

#forming parent window

root = Tk()

#making a entry column to display numbers

e = Entry(root, borderwidth = 20, width = 40)
e.grid(row = 0, column = 0, padx = 10, pady = 10, columnspan = 3)
#defining each button function
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
#defining clear button function
def button_clear():
    e.delete(0, END)

#defining the equal button for different functions

def button_equal():
    second_number = e.get()
    if math == "addition":

        e.delete(0, END)
        e.insert(0, first_number + int(second_number))


    elif math == "multiplication":

        e.delete(0, END)
        e.insert(0, first_number * int(second_number))


    elif math == "division":

        e.delete(0, END)
        e.insert(0, first_number / int(second_number))


    elif math == "subtraction":

        e.delete(0, END)
        e.insert(0, first_number - int(second_number))


    elif math == "root":

        e.delete(0, END)
        e.insert(0, first_number ** (1/2))

    elif math == "power":

        e.delete(0, END)
        e.insert(0, first_number ** int(second_number))


#making all button functions and mathematical operation functions

def button_add():
    global first_number
    global math

    first_number = int(e.get())
    math = "addition"
    e.delete(0, END)



def button_multiply():
    global first_number
    global math
    first_number = int(e.get())
    math = "multiplication"
    e.delete(0, END)


def button_subtract():
    global first_number
    global math
    first_number = int(e.get())
    math = "subtraction"
    e.delete(0, END)


def button_division():
    global first_number
    global math
    first_number = int(e.get())
    math = "division"
    e.delete(0, END)


def button_root():
    global first_number
    global math
    first_number = int(e.get())
    math = "root"
    e.delete(0, END)


def button_power():
    global first_number
    global math
    first_number = int(e.get())
    math = "power"
    e.delete(0, END)


#defining all the button in the parent window and also giving each button value and click value

button_1 = Button(root, text =1 , padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text =2 , padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text =3 , padx = 40, pady = 20, command = lambda: button_click(3))
button_4 = Button(root, text =4 , padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text =5 , padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text =6 , padx = 40, pady = 20, command = lambda: button_click(6))
button_7 = Button(root, text =7 , padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text =8 , padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text =9 , padx = 40, pady = 20, command = lambda: button_click(9))
button_0 = Button(root, text =0 , padx = 40, pady = 20, command = lambda: button_click(0))
button_add = Button(root, text ="+" , padx = 39, pady = 20, command = button_add)
button_equal = Button(root, text ="=" , padx = 91, pady = 20, command = button_equal)
button_clear = Button(root, text ="clear" , padx = 79, pady = 20, command = button_clear)
button_multiply = Button(root, text = "*", padx = 39 , pady = 20 , command = button_multiply)
button_divide = Button(root, text = "/", padx = 39, pady = 20, command = button_division)
button_subtract = Button(root, text = "-", padx = 39, pady = 20, command = button_subtract)
button_root = Button(root, text = "^1/2", padx = 39, pady = 20, command = button_root)
button_power = Button(root, text = "^", padx = 39, pady = 20, command = button_power)



#marking the position of every button
#we dont need to pack the buttons because we are using the gridd function



button_1.grid(row = 3, column =0 )
button_2.grid(row = 3, column =1 )
button_3.grid(row = 3, column =2 )

button_4.grid(row = 2, column =0 )
button_5.grid(row = 2, column =1 )
button_6.grid(row = 2, column =2 )

button_7.grid(row = 1, column =0 )
button_8.grid(row = 1, column =1 )
button_9.grid(row = 1, column =2 )

button_0.grid(row =4 , column = 0)
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)
button_clear.grid(row = 4, column = 1, columnspan = 2)


button_multiply.grid(row = 6, column = 0)
button_divide.grid(row = 6, column = 1)
button_subtract.grid(row = 7, column = 0)


button_root.grid(row = 6, column = 2)
button_power.grid(row = 7, column = 1)



# basic tkinter syntax to make parent window
root.mainloop()