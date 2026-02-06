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

def kelvin_to_celsius(kelvin):
    """
    Convert temperature from Kelvin to Celsius.
    Formula: Celsius = Kelvin - 273.15
    Args:
        kelvin (float): Temperature in Kelvin
    Returns:
        float: Temperature in Celsius
    Example:
        >>> kelvin_to_celsius(273.15)
        0.0
    """
    return kelvin - 273.15
def celsius_to_rankine(celsius):
    """
    Convert temperature from Celsius to Rankine.
    Formula: Rankine = (Celsius + 273.15) × 9/5
    Args:
        celsius (float): Temperature in Celsius
    Returns:
        float: Temperature in Rankine
    Example:
        >>> celsius_to_rankine(0)
        491.67
    """
    kelvin = celsius_to_kelvin(celsius)
    return kelvin * 9/5


def rankine_to_celsius(rankine):
    """
    Convert temperature from Rankine to Celsius.
    Formula: Celsius = (Rankine × 5/9) - 273.15
    Args:
        rankine (float): Temperature in Rankine
    Returns:
        float: Temperature in Celsius
    Example:
        >>> rankine_to_celsius(491.67)
        0.0
    """
    kelvin = rankine * 5/9
    return kelvin_to_celsius(kelvin)
__name__ = "__main__"
if __name__ == "__main__":
    # Quick test of conversion functions
    print("Temperature Converter Tests")
    print(f"0°C = 32.0 F")
    print(f"100°C = 212.0 F")
    print(f"0°C =  273.15 K")
    print(f"0°C = 491.67 R")
    print(f"491.67°R = 0.0 C")

