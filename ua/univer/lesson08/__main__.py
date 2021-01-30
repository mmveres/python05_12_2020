from tkinter import *

def click_btn():
    btn.config(text ="hello")




win = Tk()
win.title("first win")
win.geometry("300x400")

btn = Button(text= "hi", command=click_btn)
btn.pack()
win.mainloop()