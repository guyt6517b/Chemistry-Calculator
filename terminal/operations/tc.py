# (c) 2025 Guyt6517
# Educational use only. Not for resale without permission.

print(
    """
    Temperature Converter
    """
)
print(
    """
    Celsius & Farenheit:

    C To F: 1.8 * (C) + 32

    F To C: (F-32) / 1.8

    Kelvin:

    C To K: C + 273.15

    K To C: K - 273.15
    """
)
to = input("Enter the unit to translate to: ")
fro = input("Enter the unit to translate FROM")
try:
    temperature = float(input("Enter the temperature: "))
except Exception as e:
    print(e)
    exit()

if to.upper() == "F":
    if fro.upper() == "C":
        temperature = 1.8 * temperature + 32
    elif fro.upper() == "K":
        temperature = 1.8 * (temperature - 273.15) + 32
    elif fro.upper() == "F":
        temperature = temperature
elif to.upper() == "C":
    if fro.upper() == "C":
        temperature = temperature
    elif fro.upper() == "K":
        temperature = temperature - 273.15
    elif fro.upper() == "F":
        temperature = (temperature - 32) / 1.8
elif to.upper() == "K":
    if fro.upper() == "C":
        temperature = temperature + 273.15
    elif fro.upper() == "K":
        temperature = temperature
    elif fro.upper() == "F":
        temperature =  (temperature - 32) / 1.8 + 273.15
print(f"{temperature} {to.upper()}")