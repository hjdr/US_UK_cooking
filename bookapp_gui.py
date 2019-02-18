from tkinter import *
from fractions import Fraction, gcd

window = Tk()

# create list of volume measurements
volumes = ["ml (Metric)", "oz (Imperial)", "US Cups"]
volume_counter = 1

# create volume converter function
def volumer_converter():
    volume_selection = volume_metric_list.curselection()[0]
    if volume_selection == 0:
        metric_imperial_calc = int(int(volume_entry.get()) * 0.0351951)
        if float(volume_entry.get()) > 30:
            uscups_fraction = metric_to_uscups(float(volume_entry.get()))
        else:
            uscups_tablespoon = 1
        output = "{}ml is {} oz or {} US cup(s) \n".format(volume_entry.get(), metric_imperial_calc, uscups_fraction)
        volume_output.insert(END, output)

# create a function which rounds to nearest 5, used for the metric to US cups func
def round_to_five(number, base=5):
    return int(base * round(float(number) / base))

# create the function which converts metric to US cups (fractions)
def metric_to_uscups(metric_number):
    number_to_round = float(metric_number) / 250 *100
    rounded_number = round_to_five(number_to_round)
    greatest_common_divisor = gcd(rounded_number, 100)
    lowest_numerator = rounded_number / greatest_common_divisor
    lowest_denominator = 100 / greatest_common_divisor
    metric_uscups_ouput = Fraction(int(lowest_numerator), int(lowest_denominator))
    return metric_uscups_ouput

# create title for application
tite_text = Label(window, text="The US & UK food measurement converter", font="avenir 25")
tite_text.grid(row=0, column=0, columnspan=3)

# create subtitle for application
subtitle_text = Label(window, text="Here you can enter measurements such as volumes, weights and even spoons, \n and then this application will convert them into their native meansurements for you", font="avenir 10")
subtitle_text.grid(row=1, column=0, columnspan=3)

# create the title for the volume conversion section
volume_title = Label(window, text="Volume", padx=40, bg="dark grey", relief=FLAT, font="avenir", fg="white")
volume_title.grid(row=2, column=0, columnspan=3)

# create the entry field where the user enters the volume to be converted
volume_entry = StringVar()
volume_entry = Entry(window, textvariable=volume_entry)
volume_entry.grid(row=3, column=0, columnspan=1)

# create the list of volume measurements to be selected from
volume_metric_list = Listbox(window, width=10, height=3, selectbackground="grey")
for item in volumes:
    volume_metric_list.insert(volume_counter, item)
    volume_counter +=1
volume_metric_list.grid(row=volume_counter, column=1)

# create the 'convert' button for the volume conversion
volume_convert_button = Button(window, text="Convert", command=volumer_converter)
volume_convert_button.grid(row=3, column=2)


# create a frame for the volume converstion ouput field and the scrollbar
#vol_frame = Frame(window, width=600, height=600)
#vol_frame.pack(fill="both", expand=True)
#vol_frame.grid_propagate(False)
#vol_frame.grid_rowconfigure(0, weight=1)
#vol_frame.grid_columnconfigure(0, weight=1)

# create the volume conversion ouput field
volume_output = Text(window, wrap="word", font="avenir", height=10, width=20)
#vol_scrollbar = Scrollbar(volume_output)
#vol_scrollbar.config(command=volume_output.yview)
#volume_output.config(yscrollcommand=vol_scrollbar.set)
volume_output.grid(row=3, column=3, columnspan=5)
#vol_scrollbar.grid(row=3, column=4, sticky="ns")

# create the scrollbar for the volume conversion output field



window.mainloop()
