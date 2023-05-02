from tkinter import *
FONT = ("Arial", 12, "bold")
CONVERSION_FACTOR = 1.609344

# Window creation and size
window = Tk()
window.title("Mile to Km Converter")
window.geometry('250x120')
window.config(padx=15, pady=20)

# Label 1; Equal text
equal_label = Label(window, text = "is equal to", font = FONT)
equal_label.grid(column = 0, row = 1)
# Label 2; Km text
km_label = Label(window, text = "Km", font = FONT)
km_label.grid(column = 2, row = 1)
# Label 3; Miles text
miles_label = Label(window, text = "Miles", font = FONT)
miles_label.grid(column = 2, row = 0)
# Label 4; Km Conversion; Show 0 by default
conversion_label = Label(window, text = 0, font = FONT)
conversion_label.grid(column = 1, row = 1)


# Number entry box for miles
miles_input = Entry(window, width = 7, justify = 'center', font = FONT)
miles_input.grid(column = 1, row = 0)
miles_input.focus()


# Calculate button
def calc():
    """Calculate the Miles to Km conversion and display on GUI to user"""
    km_conversion = float(miles_input.get()) * CONVERSION_FACTOR
    conversion_label.config(text=f"{km_conversion:.2f}")
    
calc_btn = Button(window, text = "Calculate", command = calc, font = FONT)
calc_btn.grid(column = 1, row = 2)


# Keep window open
window.mainloop()