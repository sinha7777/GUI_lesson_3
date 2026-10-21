from tkinter import *

root = Tk()

root.geometry("400x400")
root.title("Music Player")

songframe = Frame(root)
songframe.pack(pady=10)

heading = Label(songframe,text="Now Playing",fg="black")
heading.pack(pady=5)

listbox = Listbox(songframe,height=10,width=15,bg="grey",activestyle="dotbox",font="Helvetica",fg="yellow")

listbox.insert(1,"Shape of You")
listbox.insert(2,"Believer")
listbox.insert(3,"Perfect")
listbox.insert(4,"Thunder")
listbox.insert(5,"Memories")

listbox.pack(pady=5)

bottomframe = Frame(root)
bottomframe.pack(pady=10)

b1_button = Button(bottomframe,text="Play",fg="green")
b1_button.pack(side=LEFT,padx=5)

b2_button = Button(bottomframe,text="Pause",fg="orange")
b2_button.pack(side=LEFT,padx=5)

b3_button = Button(bottomframe,text="Next",fg="blue")
b3_button.pack(side=LEFT,padx=5)

root.mainloop()