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

# Example usage:
print("Length Conversion: 10 meters to kilometers:", length_conversion(10, "meter", "kilometer"))
print("Weight Conversion: 1000 grams to kilograms:", weight_conversion(1000, "gram", "kilogram"))
print("Temperature Conversion: 100 Celsius to Fahrenheit:", temperature_conversion(100, "celsius", "fahrenheit"))