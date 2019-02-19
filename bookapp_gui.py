from tkinter import *
from fractions import Fraction, gcd

window = Tk()
window.configure(bg="#2f4f4f")

# create list of volume measurements
volumes = ["mL (Metric)", "Fluid oz (Imperial)", "US Cups"]
volume_counter = 1

# create the output field class to be used for all conversion outputs
class OutputField:
    def __init__(self, output_row, output_column, scroll_row, scroll_column):
        self.output_row = output_row
        self.output_column = output_column
        self.scroll_row = scroll_row
        self.scroll_column = scroll_column

        self.output = Text(window, wrap="word", font="avenir", height=3, width=30)
        scrollbar = Scrollbar(window)
        scrollbar.config(command=self.output.yview)
        self.output.config(yscrollcommand=scrollbar.set)
        self.output.grid(row=self.output_row, column=self.output_column)
        scrollbar.grid(row=self.scroll_row, column=self.scroll_column, sticky="nsw")

    def insert(self, text_position, conversion_output):
        self.output.insert(text_position, conversion_output)


# create the volume field class to be used for volume outputs
class VolumeField(OutputField):

    uscups_tablespoon = 1

    def volume_converter(self):
        volume_selection = volume_metric_list.curselection()[0]
        if volume_selection == 0:
            metric_imperial_calc = int(int(volume_entry.get()) * 0.0351951)
            if float(volume_entry.get()) > 30:
                uscups_output = measurement_calc((float(volume_entry.get())), 250)
                metric_output = "{}mL is {} fluid oz or {} US cup(s) \n".format(volume_entry.get(), metric_imperial_calc, uscups_output)
                OutputField.insert(self, END, metric_output)
            else:
                vol_output = "{}mL is {} fluid oz or {} tablespoon \n".format(volume_entry.get(), metric_imperial_calc, VolumeField.uscups_tablespoon)
                OutputField.insert(self, END, vol_output)
        if volume_selection == 1:
            imperial_metric_calc = int(float(volume_entry.get()) * 29.5735)
            if float(volume_entry.get()) > 0.5:
                uscups_output = measurement_calc((float(volume_entry.get())), 8)
                imperial_output = "{}oz is {}mL or {} US cup(s) \n".format(volume_entry.get(), imperial_metric_calc, uscups_output)
                OutputField.insert(self, END, imperial_output)
            else:
                vol_output = "{}oz is {}mL or {} tablespoon \n".format(volume_entry.get(), imperial_metric_calc, VolumeField.uscups_tablespoon)
                OutputField.insert(self, END, vol_output)


class MeasurementTitle:
    def __init__(self, title_text, title_row, title_column, title_columnspan):
        self.title_text = title_text
        self.title_row = title_row
        self.title_column = title_column
        self.title_columnspan = title_columnspan

        output = Label(window, text=self.title_text, padx=150, bg="dark grey", relief=FLAT, font="avenir 15 bold", fg="white", width=50)
        output.grid(row=self.title_row, column=self.title_column, columnspan=self.title_columnspan, pady=(0, 10))



def measurement_calc(input, one_cup_equiv):
    number_to_round = float(input) / one_cup_equiv * 100
    rounded_number = round_to_five(number_to_round)
    greatest_common_divisor = gcd(rounded_number, 100)
    lowest_numerator = rounded_number / greatest_common_divisor
    lowest_denominator = 100 / greatest_common_divisor
    input_uscups_fraction = Fraction(int(lowest_numerator), int(lowest_denominator))
    if lowest_numerator > lowest_denominator:
        input_uscups_cups = lowest_numerator / lowest_denominator
        return input_uscups_cups
    else:
        return input_uscups_fraction


# create a function which rounds to nearest 5, used for the metric to US cups func
def round_to_five(number, base=5):
    return int(base * round(float(number) / base))

# create the sfunction which converts metric to US cups (fractions)
# def metric_to_uscups(metric_number):
#     number_to_round = float(metric_number) / 250 *100
#     rounded_number = round_to_five(number_to_round)
#     greatest_common_divisor = gcd(rounded_number, 100)
#     lowest_numerator = rounded_number / greatest_common_divisor
#     lowest_denominator = 100 / greatest_common_divisor
#     metric_uscups_fraction = Fraction(int(lowest_numerator), int(lowest_denominator))
#     if lowest_numerator > lowest_denominator:
#         metric_uscups_cups = lowest_numerator / lowest_denominator
#         return metric_uscups_cups
#     else:
#         return metric_uscups_fraction

# create title for application
tite_text = Label(window, text="The US & UK food measurement converter", font="avenir 30 bold", fg="white", bg="#2f4f4f")
tite_text.grid(row=0, column=0, columnspan=5, padx=20, pady=(10, 0))

# create subtitle for application
subtitle_text = Label(window, text="Here you can enter measurements such as volume, mass and even spoons, then this application \n will convert them into their native meansurements", font="avenir 12", fg="white", bg="#2f4f4f")
subtitle_text.grid(row=1, column=0, columnspan=5, padx=40, pady=(0, 15))

# create the title for the volume conversion section
VolumeTitle = MeasurementTitle("Volume", 2, 0, 4)

# create the entry field where the user enters the volume to be converted
volume_entry = StringVar()
volume_entry = Entry(window, textvariable=volume_entry)
volume_entry.grid(row=3, column=0, columnspan=1)

# create the list of volume measurements to be selected from
volume_metric_list = Listbox(window, width=10, height=3, selectbackground="grey")
for item in volumes:
    volume_metric_list.insert(volume_counter, item)
    volume_counter +=1
volume_metric_list.grid(row=3, column=1)

volume_output = VolumeField(3, 3, 3, 5)


# create the 'convert' button for the volume conversion
volume_convert_button = Button(window, text="Convert", highlightbackground="#2f4f4f", command=volume_output.volume_converter, )
volume_convert_button.grid(row=3, column=2)

window.mainloop()
