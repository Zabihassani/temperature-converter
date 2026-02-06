"""
Temperature Converter Module
Provides functions to convert between Celsius, Fahrenheit, and Kelvin.
"""
Msg = "Temperature Converter Module: Provides functions to convert between Celsius, Fahrenheit, and Kelvin."

temperature_have = input ( "Enter the temperature you enter: cilsius C, fahrenheit F, or kelvin K: " )
temperature_convert = input ( "Enter the temperature you want to convert to: cilsius C, fahrenheit F, or kelvin K: " )

temperature_value = float ( input ( "Enter the temperature value you want to convert: " ) )

def convert_temperature( temperature_have, temperature_convert, temperature_value ):
    if temperature_have == "C" and temperature_convert == "F":
        return (temperature_value * 9/5) + 32
    elif temperature_have == "C" and temperature_convert == "K":
        return temperature_value + 273.15
    elif temperature_have == "F" and temperature_convert == "C":
        return (temperature_value - 32) * 5/9
    elif temperature_have == "F" and temperature_convert == "K":
        return (temperature_value - 32) * 5/9 + 273.15
    elif temperature_have == "K" and temperature_convert == "C":
        return temperature_value - 273.15
    elif temperature_have == "K" and temperature_convert == "F":
        return (temperature_value - 273.15) * 9/5 + 32
    else:
        return "Invalid input. Please enter 'C', 'F', or 'K' for both temperatures."    
print ( Msg )
converted_temperature = convert_temperature( temperature_have, temperature_convert, temperature_value )
print ( f"{temperature_value} {temperature_have} is equal to {converted_temperature} {temperature_convert}." )


