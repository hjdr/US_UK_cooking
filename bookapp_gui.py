from tkinter import *
from fractions import Fraction, gcd

window = Tk()
window.configure(bg="#2f4f4f")

# create list of measurements
volumes = ["mL (Metric)", "Fluid oz (Imperial)", "US Cups"]
mass = ["Mass oz (Imperial)", "grams (Metric)"]
spoons = ["Teaspoons", "Tablespoons", "mL (Metric)"]

# create the output field class to be used for all conversion outputs
class OutputField:
    def __init__(self, output_row, output_column, scroll_row, scroll_column):
        self.output_row = output_row
        self.output_column = output_column
        self.scroll_row = scroll_row
        self.scroll_column = scroll_column

        self.output = Text(window, wrap="word", font="avenir", height=3, width=33)
        scrollbar = Scrollbar(window)
        scrollbar.config(command=self.output.yview)
        self.output.config(yscrollcommand=scrollbar.set)
        self.output.grid(row=self.output_row, column=self.output_column)
        scrollbar.grid(row=self.scroll_row, column=self.scroll_column, sticky="nsw")

    def insert(self, text_position, conversion_output):
        self.output.insert(text_position, conversion_output)


# create the volume field child class to be used for volume conversions
class VolumeField(OutputField):

    uscups_tablespoon = 1
    ml_uscup_equiv = 250
    oz_uscup_equiv = 8

    def volume_converter(self):
        volume_selection = VolumeList.measurement_list.curselection()[0]
        if volume_selection == 0:
            metric_imperial_calc = int(int(VolumeEntry.measurement_entry.get()) * 0.0351951)
            if float(VolumeEntry.measurement_entry.get()) > 30:
                uscups_output = measurement_to_uscup_calc((float(VolumeEntry.measurement_entry.get())), VolumeField.ml_uscup_equiv)
                metric_output = "{}mL is {} fluid oz or {} US cup(s) \n".format(VolumeEntry.measurement_entry.get(), metric_imperial_calc, uscups_output)
                OutputField.insert(self, END, metric_output)
            else:
                vol_output = "{}mL is {} fluid oz or {} tablespoon \n".format(VolumeEntry.measurement_entry.get(), metric_imperial_calc, VolumeField.uscups_tablespoon)
                OutputField.insert(self, END, vol_output)
        if volume_selection == 1:
            imperial_metric_calc = int(float(VolumeEntry.measurement_entry.get()) * 29.5735)
            if float(VolumeEntry.measurement_entry.get()) > 0.5:
                uscups_output = measurement_to_uscup_calc((float(VolumeEntry.measurement_entry.get())), VolumeField.oz_uscup_equiv)
                imperial_output = "{}oz is {}mL or {} US cup(s) \n".format(VolumeEntry.measurement_entry.get(), imperial_metric_calc, uscups_output)
                OutputField.insert(self, END, imperial_output)
            else:
                vol_output = "{}oz is {}mL or {} tablespoon \n".format(VolumeEntry.measurement_entry.get(), imperial_metric_calc, VolumeField.uscups_tablespoon)
                OutputField.insert(self, END, vol_output)
        if volume_selection == 2:
            uscup_to_oz = uscup_to_measurement_calc(VolumeEntry.measurement_entry.get(), VolumeField.oz_uscup_equiv)
            uscup_to_ml = uscup_to_measurement_calc(VolumeEntry.measurement_entry.get(), VolumeField.ml_uscup_equiv)
            uscup_output = "{} US Cup is {}mL or {}oz \n".format(VolumeEntry.measurement_entry.get(), uscup_to_ml, uscup_to_oz)
            OutputField.insert(self, END, uscup_output)


# create the mass field child class to be used for mass conversions
class MassField(OutputField):
    def mass_converter(self):
        mass_selection = MassList.measurement_list.curselection()[0]
        if mass_selection == 0:
            oz_gram_calc = int(int(MassEntry.measurement_entry.get()) * 28.3495)
            oz_output = "{}oz is {} grams \n".format(MassEntry.measurement_entry.get(), oz_gram_calc)
            OutputField.insert(self, END, oz_output)
        if mass_selection == 1:
            gram_oz_calc = int(int(MassEntry.measurement_entry.get()) * 0.035274)
            gram_output = "{} grams is {}oz \n".format(MassEntry.measurement_entry.get(), gram_oz_calc)
            OutputField.insert(self, END, gram_output)


# create the Spoons field child class to be used for spoons conversions
class SpoonsField(OutputField):
    def spoons_converter(self):
        spoons_selection = SpoonsList.measurement_list.curselection()[0]
        if spoons_selection == 0:
            teaspoon_tablespoon_calc = round(float(int(SpoonsEntry.measurement_entry.get()) * 0.33333), 1)
            teaspoon_ml_calc = int(int(SpoonsEntry.measurement_entry.get()) * 5.91939)
            teaspoon_output = "{} teaspoon(s) is {} tablespoon(s) or {}mL \n".format(SpoonsEntry.measurement_entry.get(), teaspoon_tablespoon_calc, teaspoon_ml_calc)
            OutputField.insert(self, END, teaspoon_output)
        if spoons_selection == 1:
            tablespoon_teaspoon_calc = int(int(SpoonsEntry.measurement_entry.get()) * 3)
            tablespoon_ml_calc = int(int(SpoonsEntry.measurement_entry.get()) * 17.7582)
            tablespoon_output = "{} tablespoon(s) is {} teaspoon(s) or {}mL \n".format(SpoonsEntry.measurement_entry.get(), tablespoon_teaspoon_calc, tablespoon_ml_calc)
            OutputField.insert(self, END, tablespoon_output)
        if spoons_selection == 2:
            ml_teaspoon_calc = round(float(int(SpoonsEntry.measurement_entry.get()) * 0.168936), 1)
            ml_tablespoon_calc = round(float(int(SpoonsEntry.measurement_entry.get()) * 0.0563121), 1)
            ml_output = "{}mL is {} teaspoon(s) or {} tablespoon(s) \n".format(SpoonsEntry.measurement_entry.get(), ml_teaspoon_calc, ml_tablespoon_calc)
            OutputField.insert(self, END, ml_output)


# create a title class for volume/mass etc
class MeasurementTitle:
    def __init__(self, title_text, title_row, title_column):
        self.title_text = title_text
        self.title_row = title_row
        self.title_column = title_column

        output = Label(window, text=self.title_text, padx=150, bg="dark grey", relief=FLAT, font="avenir 15 bold", fg="white", width=50)
        output.grid(row=self.title_row, column=self.title_column, columnspan=6, pady=10, padx=10)


# create the entry class where the user enters the measurement to be converted
class MeasurementEntry:
    def __init__(self, entry_row, entry_column, entry_columnspan):
        self.entry_row = entry_row
        self.entry_column = entry_column
        self.entry_columnspan = entry_columnspan

        self.measurement_entry = StringVar()
        self.measurement_entry = Entry(window, textvariable=self.measurement_entry)
        self.measurement_entry.grid(row=self.entry_row, column=self.entry_column, columnspan=self.entry_columnspan)


# create the list of volume measurements to be selected from
class MeasurementList:

    counter = 1

    def __init__(self, list, list_row, list_column):
        self.list = list
        self.list_row = list_row
        self.list_column = list_column

        self.measurement_list = Listbox(window, width=15, height=3, selectbackground="grey")
        for item in list:
            self.measurement_list.insert(MeasurementList.counter, item)
            MeasurementList.counter +=1
        self.measurement_list.grid(row=self.list_row, column=self.list_column)


# create the class 'convert' button for the measurement conversion
class MeasurementButton:
    def __init__(self, class_measurement_converter, button_row, button_column):
        self.class_measurement_converter = class_measurement_converter
        self.button_row = button_row
        self.button_column = button_column

        convert_button = Button(window, text="Convert", highlightbackground="#2f4f4f", command=self.class_measurement_converter)
        convert_button.grid(row=self.button_row, column=self.button_column)

# create the volume child class which calculates the volume outputs
VolumeOutput = VolumeField(3, 3, 3, 5)


# create the mass child class which calculates the mass outputs
MassOutput = MassField(5, 3, 5, 5)


# create the mass child class which calculates the mass outputs
SpoonsOutput = SpoonsField(7, 3, 7, 5)


# create a function which calculates an input and outputs it in US Cups
def measurement_to_uscup_calc(input, one_cup_equiv):
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


# create a function which calculates an input and outputs it in metric/imperial
def uscup_to_measurement_calc(input, one_cup_equiv):
    numerator = input[0]
    denominator = input[2:]
    get_percent = int(numerator) / int(denominator) * 100
    measurement = get_percent / 100 * one_cup_equiv
    return int(measurement)


# create a function which rounds to nearest 5, used for the metric to US cups func
def round_to_five(number, base=5):
    return int(base * round(float(number) / base))


# create title for application
tite_text = Label(window, text="The US & UK food measurement converter", font="avenir 30 bold", fg="white", bg="#2f4f4f")
tite_text.grid(row=0, column=0, columnspan=5, padx=20, pady=(10, 0))


# create subtitle for application
subtitle_text = Label(window, text="Here you can enter measurements such as volume, mass and even spoons, then this application \n will convert them into their native meansurements", font="avenir 14", fg="white", bg="#2f4f4f")
subtitle_text.grid(row=1, column=0, columnspan=5, padx=40, pady=(0, 15))


# create the title for the volume conversion section
VolumeTitle = MeasurementTitle("Volume", 2, 0)


# create entry child class where the user enters the volume to be converted
VolumeEntry = MeasurementEntry(3, 0, 1)


# create list child class of volume measurements which user selects from
VolumeList = MeasurementList(volumes, 3, 1)


# create the 'convert' child class button for the volume conversion
VolumeButton = MeasurementButton(VolumeOutput.volume_converter, 3, 2)


# create the title for the weight conversion section
MassTitle = MeasurementTitle("Mass", 4, 0)


# create entry child class where the user enters the mass to be converted
MassEntry = MeasurementEntry(5, 0, 1)


# create list child class of mass measurements which user selects from
MassList = MeasurementList(mass, 5, 1)


# create the 'convert' child class button for the mass conversion
MassButton = MeasurementButton(MassOutput.mass_converter, 5, 2)


# create the title for the Spoons conversion section
SpoonsTitle = MeasurementTitle("Spoons", 6, 0)


# create entry child class where the user enters the Spoons to be converted
SpoonsEntry = MeasurementEntry(7, 0, 1)


# create list child class of Spoons measurements which user selects from
SpoonsList = MeasurementList(spoons, 7, 1)


# create the 'convert' child class button for the Spoons conversion
SpoonsButton = MeasurementButton(SpoonsOutput.spoons_converter, 7, 2)


# create the title for the notes section
NotesTitle = MeasurementTitle("Notes", 9, 0)

# create notes section
notes = Text(window, wrap="word", font="avenir", height=10, width=83)
notes_scrollbar = Scrollbar(window)
notes_scrollbar.config(command=notes.yview)
notes.config(yscrollcommand=notes_scrollbar.set)
notes.grid(row=10, column=0, columnspan=4, pady=(4, 10))
notes_scrollbar.grid(row=10, column=5, sticky="nsw")


window.mainloop()
