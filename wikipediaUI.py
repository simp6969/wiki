from tkinter import  Label, Button, Tk, Entry
import wikipedia

root = Tk()

def getEntryText():
    val = (entry.get())
    root = Tk()
    labelForResult = Label(root, text=wikipedia.summary(val),wraplength=400)
    labelForResult.pack()
    root.mainloop()


label = Label(root, text="search anything from wikipedia")
label.grid(row=1, column=1)

entry = Entry(root)
entry.grid(row=2, column=1)

button = Button(root, text="search",command=getEntryText)
button.grid(row= 3, column=1)


root.mainloop()