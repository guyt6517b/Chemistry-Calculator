# (c) 2025 Guyt6517
# Educational use only. Not for resale without permission.

print(
    """
    Pressure unit converter
    """
)

pressure_conversions = {
    "pa": 1,
    "kpa": 1e3,
    "mpa": 1e6,
    "bar": 1e5,
    "atm": 101325,
    "psi": 6894.757,
    "torr": 133.322,
}

def convert_pressure(value: float, from_unit: str, to_unit: str) -> float:
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    if from_unit not in pressure_conversions or to_unit not in pressure_conversions:
        raise ValueError("Unsupported unit")
    
    value_in_pa = value * pressure_conversions[from_unit]

    return value_in_pa / pressure_conversions[to_unit]

val = float(input("What is the value? "))
fro = input("What is the unit you are converting from? ")
to = input("What is the unit you are converting to? ")

print(convert_pressure(val, fro, to))