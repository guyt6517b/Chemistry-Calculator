# (c) 2025 Guyt6517
# Educational use only. Not for resale without permission.

import inflect

p = inflect.engine()

print(
    """
    The Imperial to Metric Converter (BETA)
    """
)

# --- Conversion ratios ---
# All imperial units -> inches
imperial_to_inches = {
    "inch": 1,
    "inches": 1,
    "foot": 12,
    "feet": 12,
    "yard": 36,
    "yards": 36,
    "mile": 5280 * 12,
    "miles": 5280 * 12
}



# Metric prefixes + their 10^exponent values
exponents = {
    "quecto": -30, "ronto": -27, "yocto": -24, "zepto": -21, "atto": -18, "femto": -15,
    "pico": -12, "nano": -9, "micro": -6, "milli": -3, "centi": -2, "deci": -1,
    "base": 0,
    "deca": 1, "hecto": 2, "kilo": 3, "mega": 6, "giga": 9, "tera": 12,
    "peta": 15, "exa": 18, "zetta": 21, "yotta": 24, "ronna": 27, "quetta": 30
}


def imperial_to_meters(unit: str, value: float) -> float:
    """Convert any imperial length to meters."""
    if unit not in imperial_to_inches:
        raise ValueError(f"Unsupported imperial unit: {unit}")
    inches = value * imperial_to_inches[unit]
    return inches / 39.37 # 1 inch = 0.0254 m


def metric_convert(origin: str, dest: str, value: float) -> float:
    """Convert between SI prefixes (all based on meters)."""
    if origin not in exponents or dest not in exponents:
        raise ValueError(f"Unsupported metric prefix: {origin} or {dest}")
    power_diff = exponents[origin] - exponents[dest]
    return value * (10 ** power_diff)


# --- Main program ---
fro = input("Enter the imperial unit (inch, foot, yard, mile): ").lower()
value = float(input("Enter the value: "))
to = input(f"You are converting {value} {p.plural(fro)} to what metric unit? ").lower()

# Step 1: Imperial → meters
meters = imperial_to_meters(fro, value)

# Step 2: meters → chosen metric
converted = metric_convert("base", to, meters)

print(f"{value} {p.plural(fro)} = {converted} {p.plural(to)}")