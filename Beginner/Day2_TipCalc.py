# Tip Calculator
import string
print("Welcome to the tip calculator.")

# Accepting inputs for the bill
total_input = str(input("What was the total bill? "))
people = int(input("How many people split the bill? "))
tip_input = str(input("What percentage tip would you like to give? "))

# Converting total into a Float value
total =  ''
for i in total_input:
    if i in string.digits or i == ".":
        total += str(i)
total = float(total)

# Converting tip value into Float decimal equivalent, stripping % symbol as well
tip = '0.'
for i in tip_input:
    if i in string.digits:
        tip += str(i)
tip = float(tip)

# Calculating your split
your_split = round(total / people, 2)
your_tip = round(your_split * tip, 2)
your_split_combined = your_split + your_tip
split_rounded = format(round(your_split_combined, 2), '.2f')

# Final output of calculations
print(f"Each person should pay: ${split_rounded}")