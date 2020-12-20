from tkinter import *
import time
import datetime
root = Tk()

def get_time():

    time_ = time.strftime("%I:%M:%S:%p")
    clock.config(text = time_)
    clock.after(10, get_time)
clock = Label(root, font = ('time' , 50 , "bold"), bg = "#ff9999")
clock.pack()

get_time()

def get_date():
    date = datetime.date.today()
    calender.config(text = date)
calender = Label(root, font = ('date', 58, 'bold'), bg = "#ff9999")
calender.pack()

get_date()

root.mainloop()
