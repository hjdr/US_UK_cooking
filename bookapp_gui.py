from Tkinter import *

window = Tk()

volumes = ["Metric", "Imperial", "US Cups"]
volume_counter = 1

def volumer_converter():
    miles = int(volume_entry.get())*1.6
    t1.insert(END, miles)

tite_text = Label(window, text="The US & UK food measurement converter", font="avenir 25")
tite_text.grid(row=0, column=0, columnspan=3)

subtitle_text = Label(window, text="Here you can enter measurements such as volumes, weights and even spoons, \n and then this application will convert them into their native meansurements for you", font="avenir 10")
subtitle_text.grid(row=1, column=0, columnspan=3)

volume_title = Label(window, text="Volume", padx=40, bg="dark grey", relief=FLAT, font="avenir", fg="white")
volume_title.grid(row=2, column=0, columnspan=3)

volume_entry = StringVar()
volume_entry = Entry(window, textvariable=volume_entry)
volume_entry.grid(row=3, column=0, columnspan=1)

volume_metric_list = Listbox(window, width=10, height=3, selectbackground="grey")
for item in volumes:
    print volume_metric_list.insert(volume_counter, item)
    volume_counter +=1
volume_metric_list.grid(row=volume_counter, column=1)

b1 = Button(window, text="Convert", command=volumer_converter)
b1.grid(row=3, column=2)


t1 = Text(window, height=1, width=20, bd=2)
t1.grid(row=3, column=3)

window.mainloop()
