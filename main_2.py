from tkinter import *

root = Tk()

root.geometry("400x400")
root.title("listbox")

heading = Label(root,text = "Favourite food items",fg= "black")
heading.pack(pady=5)

listbox = Listbox(root,height=10,width=15,bg="grey",activestyle="dotbox",font="Helvectia",fg="yellow")

listbox.insert(1,"Nachos")
listbox.insert(2,"Cake")
listbox.insert(3,"Pizza")
listbox.insert(4,"Pasta")
listbox.insert(5,"Chips")

listbox.pack(pady=5)

root.mainloop()