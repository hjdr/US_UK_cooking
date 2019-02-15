from Tkinter import *
from fractions import Fraction, gcd

window = Tk()

volumes = ["ml (Metric)", "oz (Imperial)", "US Cups"]
volume_counter = 1

def volumer_converter():
    volume_selection = volume_metric_list.curselection()[0]
    if volume_selection == 0:
        #metric_imperial_calc = int(volume_entry.get()) * 0.0351951
        if float(volume_entry.get()) > 30:
            number_to_round = Fraction(float(volume_entry.get()) / 250 *100)
            rounded_number = round_to_five(number_to_round)
            greatest_common_divisor = gcd(rounded_number, 100)
            lowest_numerator = rounded_number / greatest_common_divisor
            lowest_denominator = 100 / greatest_common_divisor
            metric_uscups_calc = Fraction(lowest_numerator, lowest_denominator)
    volume_output.insert(END, metric_uscups_calc)
    #miles = int(volume_entry.get())*1.6


def round_to_five(number, base=5):
    return int(base * round(float(number) / base))

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
#print(volume_selection)


volume_convert_button = Button(window, text="Convert", command=volumer_converter)
volume_convert_button.grid(row=3, column=2)


volume_output = Text(window, height=1, width=20, bd=2)
volume_output.grid(row=3, column=3)

window.mainloop()
