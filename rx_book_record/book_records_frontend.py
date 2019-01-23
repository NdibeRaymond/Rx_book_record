from tkinter import *
import book_records_backend


def view_command():
    box.delete(0,END)
    gate = book_records_backend.view_all()
    title_entry.delete(0,END)
    author_entry.delete(0,END)
    year_entry.delete(0,END)
    isbn_entry.delete(0,END)
    for each in gate:
        box.insert(END,each)

def search_command():
    box.delete(0,END)
    gate = book_records_backend.search(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    title_entry.delete(0,END)
    author_entry.delete(0,END)
    year_entry.delete(0,END)
    isbn_entry.delete(0,END)
    if gate == []:
        box.insert(END,"Input value/values to search!!")
    else:
        for each in gate:
            box.insert(END,each)

def add_command():
    box.delete(0,END)
    book_records_backend.add_record(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    title_entry.delete(0,END)
    author_entry.delete(0,END)
    year_entry.delete(0,END)
    isbn_entry.delete(0,END)
    box.insert(END,"Record added succesfully")

def delete_command():
    box.delete(0,END)
    gate = book_records_backend.search(title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    title_entry.delete(0,END)
    author_entry.delete(0,END)
    year_entry.delete(0,END)
    isbn_entry.delete(0,END)
    for each in gate:
        book_records_backend.delete(each[0])
    box.insert(END,"Record deleted succesfully")

def update_command():
    box.delete(0,END)
    book_records_backend.update(selected_tuple[0],title_entry.get(),author_entry.get(),year_entry.get(),isbn_entry.get())
    title_entry.delete(0,END)
    author_entry.delete(0,END)
    year_entry.delete(0,END)
    isbn_entry.delete(0,END)
    box.insert(END,"Record updated succesfully")

def get_selected_row(event):
    global selected_tuple
    index = box.curselection()[0]
    selected_tuple = box.get(index)
    title_entry.delete(0,END)
    author_entry.delete(0,END)
    year_entry.delete(0,END)
    isbn_entry.delete(0,END)
    title_entry.insert(END,selected_tuple[1])
    author_entry.insert(END,selected_tuple[2])
    year_entry.insert(END,selected_tuple[3])
    isbn_entry.insert(END,selected_tuple[4])

window = Tk()
window.wm_title("RX BookStore")

l1 = Label(window,text = "Title")
l1.grid(row = 0,column = 0)

l2 = Label(window,text = "Author")
l2.grid(row = 0,column = 2)

l3 = Label(window,text = "Year")
l3.grid(row = 1,column = 0)

l4 = Label(window,text = "ISBN")
l4.grid(row = 1,column = 2)

title_entry = Entry(window,textvariable = StringVar())
title_entry.grid(row = 0,column = 1)

author_entry = Entry(window,textvariable = StringVar())
author_entry.grid(row = 0,column = 3)

year_entry = Entry(window,textvariable = StringVar())
year_entry.grid(row = 1,column = 1)

isbn_entry = Entry(window,textvariable = StringVar())
isbn_entry.grid(row = 1,column = 3)

box = Listbox(window,height = 6,width = 50)
box.grid(row = 2,column = 1,rowspan = 5,columnspan = 3)
box.bind("<<ListboxSelect>>",get_selected_row)

s = Scrollbar(window)
s.grid(row = 2, column = 0,rowspan = 5)

box.configure(yscrollcommand = s.set)

s.configure(command = box.yview)

b1 = Button(window,text = "View all",command = view_command,width = 12)
b1.grid(row = 0,column = 4)

b2 = Button(window,text = "Search Entry",command = search_command,width = 12)
b2.grid(row = 1,column = 4)

b3 = Button(window,text = "Add Entry",command = add_command,width = 12)
b3.grid(row = 3,column = 4)

b4 = Button(window,text = "Update",command = update_command,width = 12)
b4.grid(row = 4,column = 4)

b5 = Button(window,text = "Delete",command = delete_command,width = 12)
b5.grid(row = 5,column = 4)

b6 = Button(window,text = "Close",command = window.destroy,width = 12)
b6.grid(row = 6,column = 4)

window.mainloop()
