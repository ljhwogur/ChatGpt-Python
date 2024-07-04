import tkinter as tk
from tkinter import ttk

def length_conversion(value, from_unit, to_unit):
    length_units = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254
    }
    
    if from_unit not in length_units or to_unit not in length_units:
        return "Invalid length unit"

    return value * (length_units[to_unit] / length_units[from_unit])

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "pound": 0.453592,
        "ounce": 0.0283495
    }
    
    if from_unit not in weight_units or to_unit not in weight_units:
        return "Invalid weight unit"
    
    return value * (weight_units[to_unit] / weight_units[from_unit])

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15

    if from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return ((value - 32) * 5/9) + 273.15

    if from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return ((value - 273.15) * 9/5) + 32
    
    return "Invalid temperature unit"

def convert():
    try:
        value = float(entry_value.get())
        from_unit = combo_from_unit.get()
        to_unit = combo_to_unit.get()
        category = combo_category.get()

        if category == "Length":
            result = length_conversion(value, from_unit, to_unit)
        elif category == "Weight":
            result = weight_conversion(value, from_unit, to_unit)
        elif category == "Temperature":
            result = temperature_conversion(value, from_unit, to_unit)
        else:
            result = "Invalid category"

        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input")
        
# GUT setup
root = tk.Tk()
root.title("Unit Converter")

# Entry for value
tk.Label(root, text="Value:").grid(row=0, column=0)
entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1)

# Combobaox for category
tk.Label(root, text="Category:").grid(row=1, column=0)
combo_category = ttk.Combobox(root, values=["Length", "Weight", "Temperature"])
combo_category.grid(row=1, column=1)
combo_category.current(0)

# Combobox for from_unit
tk.Label(root, text="From Unit:").grid(row=2, column=0)
combo_from_unit = ttk.Combobox(root)
combo_from_unit.grid(row=2, column=1)

# Combobox for to_unit
tk.Label(root, text="To Unit").grid(row=3, column=0)
combo_to_unit = ttk.Combobox(root)
combo_to_unit.grid(row=3, column=1)

# Update units based on category
def update_units(event):
    category = combo_category.get()
    if category == "Length":
        units = ["meter", "kilometer", "centimeter", "millimeter", "mile", "yard", "foot", "inch" ]
    elif category == "Weight":
        units = ["Kilogram", "gram", "miligram", "pound", "ounce"]
    elif category == "Temperature":
        units = ["celsius", "fahrenheit", "kelvin"]
    combo_from_unit.config(values=units)
    combo_to_unit.config(values=units)
    combo_from_unit.current(0)
    combo_from_unit.current(0)
    
combo_category.bind("<<ComboboxSelected>>", update_units)

# Button to convert
btn_convert = tk.Button(root, text="Convert", command=convert)
btn_convert.grid(row=4, column=0, columnspan=2)

# Label for result
label_result = tk.Label(root, text="Result: ")
label_result.grid(row=5, column=0, columnspan=2)

# Initialize units
update_units(None)

root.mainloop()