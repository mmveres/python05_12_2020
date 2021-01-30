import csv
from tkinter import *
from tkinter import messagebox, filedialog

from ua.univer.lesson07.inheritance.people import *


def get_humans():
    st1 = Student("Tom", 20, 1)
    doc1 = Doctor("Haus", 50, 66666666)
    fight1 = Fighter("BrusLi",30,99,50)
    fight2 = Fighter("Conan",30,50,40)
    vet1 = Vetirinar("AyBolit", 70, 77777777)
    ped1 = Pediatr("P",30,88888888)
    fd = FighterDoc("F1",1,22222222,3,4)
    return [st1,doc1,fight1,fight2,vet1,ped1,fd]

def view_click():
    for human in get_humans():
        languages_listbox.insert(END,human.__str__())

def open_click():
    filename = filedialog.askopenfilename()
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            languages_listbox.insert(END,f"{row['name']} - {row['age']}")

def new_click():
    new_win_human = Tk()
    new_win_human.title("new_win_human")
    new_win_human.geometry("300x250")
    name = StringVar()
    surname = StringVar()

    name_label = Label(text="Введите имя:")
    surname_label = Label(text="Введите фамилию:")

    name_label.grid(row=0, column=0, sticky="w")
    surname_label.grid(row=1, column=0, sticky="w")

    name_entry = Entry(textvariable=name)
    surname_entry = Entry(textvariable=surname)
    name = name_entry.get()
    st = Student(name, 20, 1)
    languages_listbox.insert(END,st.__str__())
    name_entry.grid(row=0,column=1, padx=5, pady=5)
    surname_entry.grid(row=1,column=1, padx=5, pady=5)

    new_win_human.mainloop()

def edit_click():
    messagebox.showinfo("GUI Python", "Нажата опция Edit")

root = Tk()
root.title("GUI на Python")
root.geometry("300x250")

main_menu = Menu()

file_menu = Menu()
file_menu.add_command(label="New", command = new_click)
file_menu.add_command(label="Save")
file_menu.add_command(label="Open", command = open_click)
file_menu.add_separator()
file_menu.add_command(label="Exit")


main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Edit", command = edit_click)
main_menu.add_cascade(label="View", command = view_click)

root.config(menu=main_menu)
languages_listbox = Listbox()



languages_listbox.pack()
root.mainloop()