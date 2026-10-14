from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Chocos and Icecreams")

heading = Label(text="Chocos and Icecreams",font=50)
heading.pack(pady=15)

topframe = Frame(root)
topframe.pack(pady=10)

b1_button = Button(topframe,text="Choco",fg="brown",bg="tan")
b1_button.pack(side=LEFT,padx=5)

b2_button = Button(topframe,text="Dark Choco",fg="black",bg="tan")
b2_button.pack(side=LEFT,padx=5)

b3_button = Button(topframe,text="White Choco",fg="dark blue",bg="tan")
b3_button.pack(side=LEFT,padx=5)

bottomframe = Frame(root)
bottomframe.pack(pady=10)

b4_button = Button(bottomframe,text="Tiramisu",fg="light blue",bg="dark blue")
b4_button.pack(side="bottom",pady=5)

b5_button = Button(bottomframe,text="Choco Icecream",fg="brown",bg="pink")
b5_button.pack(side=BOTTOM,pady=5)

b6_button = Button(bottomframe,text="Strawberry IceCream",fg="pink",bg="purple")
b6_button.pack(side=BOTTOM,pady=5)

root.mainloop()
