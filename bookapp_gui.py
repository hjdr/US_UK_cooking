from Tkinter import *

window = Tk()

def km_to_miles():
    miles = int(e1_value.get())*1.6
    t1.insert(END, miles)

tite_text = Label(window, text="The US to UK food measurement converter", font="avenir 25")
tite_text.grid(row=0, column=0, columnspan=3)

b1 = Button(window, text="Execute", command=km_to_miles)
b1.grid(row=1, column=1)

kg_text = Label(window, text="Kilograms", padx=40, bg="dark grey", relief=FLAT, font="avenir", fg="white")
kg_text.grid(row=1, column=0)



e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=1, column=2)

t1 = Text(window, height=1, width=40)
t1.grid(row=1, column=3)

window.mainloop()
