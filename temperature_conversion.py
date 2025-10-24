#Task: Temperature Conversion
#   Create a Python program that converts temperatures between Celsius and Fahrenheit. 
#   Prompt the user to enter a temperature value and the unit of measurement,
#   and then display the converted temperature.

import re
#specifing the input pattern
pattern = r"(\-?\d+\.?\d*)([CcFf])$"
inputtempature = input("Enter the tempature in Celsius or Fahrenheits :")
match = re.match(pattern,inputtempature)
if match:
    tempature = float(match.group(1))
    unit = match.group(2).upper()
    #print(type(tempature))
    #print(type(unit))
    if unit == "C":
        fahrenheit = (tempature * 9/5) + 32
        print(f"{tempature}{unit} in Fahrenheit :- {fahrenheit:g} F")
    elif unit == "F":
        celsius = (tempature - 32) * 5/9
        print(f"{tempature}{unit} in Celsius :- {celsius:g} C")
else:
    print("not a valid input")
