import streamlit as st

def length_converter(value, from_unit, to_unit):
    """Convert between length units"""
    length_units = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }
    
    # Convert to meters first, then to target unit
    value_in_meters = value * length_units[from_unit]
    return value_in_meters / length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    """Convert between weight units"""
    weight_units = {
        'kilograms': 1,
        'grams': 0.001,
        'milligrams': 0.000001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    
    # Convert to kilograms first, then to target unit
    value_in_kg = value * weight_units[from_unit]
    return value_in_kg / weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    """Convert between temperature units"""
    if from_unit == to_unit:
        return value
    
    # Convert to Celsius first
    if from_unit == 'Celsius':
        celsius = value
    elif from_unit == 'Fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'Kelvin':
        celsius = value - 273.15
    
    # Convert from Celsius to target unit
    if to_unit == 'Celsius':
        return celsius
    elif to_unit == 'Fahrenheit':
        return (celsius * 9/5) + 32
    elif to_unit == 'Kelvin':
        return celsius + 273.15

def main():
    st.title("Unit Converter")
    
    # Conversion type selection
    conversion_type = st.selectbox(
        "Select conversion type",
        ["Length", "Weight", "Temperature"]
    )
    
    # Input value
    value = st.number_input("Enter value", value=0.0)
    
    # Unit selection based on conversion type
    if conversion_type == "Length":
        units = ['meters', 'kilometers', 'centimeters', 'millimeters', 
                'miles', 'yards', 'feet', 'inches']
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units, index=1)
        
        if st.button("Convert"):
            result = length_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    
    elif conversion_type == "Weight":
        units = ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces']
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units, index=1)
        
        if st.button("Convert"):
            result = weight_converter(value, from_unit, to_unit)
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    
    elif conversion_type == "Temperature":
        units = ['Celsius', 'Fahrenheit', 'Kelvin']
        from_unit = st.selectbox("From", units)
        to_unit = st.selectbox("To", units, index=1)
        
        if st.button("Convert"):
            result = temperature_converter(value, from_unit, to_unit)
            st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

if __name__ == "__main__":
    main()