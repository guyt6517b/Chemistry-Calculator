# (c) 2025 Guyt6517
# Educational use only. Not for resale without permission.

print(
    """
    Metric to Metric Unit Converter
    """
)
def run():
    def doConver(origin, desti, value):
        with open("conversions.txt", "r") as conversions:
            conversions = str(conversions.read()).split("\n")
        for n in range(0,24):
            if origin == prefixs[n]:
                fromNum = float(conversions[n])
                for n in range(0,24):
                    if desti == prefixs[n]:
                        toNum = float(conversions[n])
                        value = value * (fromNum / toNum)
                        return value
    #             0          1       2        3       4       5      6       7       8       9        10       11      12      13      14        15       16      17       18      19      20      21       22       23        24
    prefixs = ['quetta', 'ronna', 'yotta', 'zetta', 'exa', 'peta', 'tera', 'giga', 'mega', 'kilo', 'hecto', 'deca', 'base', 'deci', 'centi', 'milli', 'micro', 'nano', 'pico', 'femto', 'atto', 'zepto', 'yocto', 'ronto', 'quecto']
    print(
        #Pre  Abr  Value                         Sc
        """
        Quetta Q 1000000000000000000000000000000 10^30 Nonillion

        Ronna R 1000000000000000000000000000 10^27 Octillion

        Yotta Y 1000000000000000000000000 10^24 Septillion

        Zetta Z 1000000000000000000000 10^21 Sextillion

        Exa E 1000000000000000000 10^18 Quintillion

        Peta P 1000000000000000 10^15 Quadrillion

        Tera T 1000000000000 10^12 Trillion

        Giga G 1000000000 10^9 Billion

        Mega M 1000000 10^6 Million

        Kilo k 1000 10^3 Thousand

        Hecto h 100 10^2 Hundred

        Deca da 10 10^1 Ten

        Base BASE 1 10^0 One

        Deci d 0.1 10^-1 Tenth

        Centi c 0.01 10^-2 Hundredth

        Milli m 0.001 10^-3 Thousandth

        Micro μ 0.000001 10^-6 Millionth

        Nano n 0.000000001 10^-9 Billionth

        Pico p 0.000000000001 10^-12 Trillionth

        Femto f 0.000000000000001 10^-15 Quadrillionth

        Atto a 0.000000000000000001 10^-18 Quintillionth

        Zepto z 0.000000000000000000001 10^-21 Sextillionth

        Yocto y 0.000000000000000000000001 10^-24 Septillionth

        Ronto r 0.000000000000000000000000001 10^-27 Octillionth

        Quecto q 0.000000000000000000000000000001 10^-30 Nonillionth
        """
    )

    exponents = {
        "Base": 0,
        "Deci": -1, "Centi": -2, "Milli": -3, "Micro": -6, "Nano": -9, "Pico": -12, "Femto": -15, "Atto": -18,
        "Zepto": -21, "Yocto": -24,
        "Deca": 1, "Hecto": 2, "Kilo": 3, "Mega": 6, "Giga": 9, "Tera": 12, "Peta": 15, "Exa": 18,
        "Zetta": 21, "Yotta": 24, "Ronna": 27, "Quetta": 30, "Ronto": -27, "Quecto": -30
    }

    def doConver(origin: str, desti: str, value: float):
        """Convert between SI-prefixed values (preserves decimals and allows small/large numbers)."""
        if origin not in exponents or desti not in exponents:
            return "Invalid prefix"

        from_exp = exponents[origin]
        to_exp = exponents[desti]

        # convert to base units
        base_value = value * (10 ** from_exp)
        # scale
        converted = base_value / (10 ** to_exp)
        return converted

    def parse_number(s: str) -> float:
        """Parse numbers in standard or scientific notation:
        Accepts 1e3, 2.5E-6, or 1*10^3."""
        s = s.replace(" ", "")
        if "*10^" in s:
            try:
                base, exp = s.split("*10^")
                return float(base) * (10 ** float(exp))
            except ValueError:
                raise ValueError("Invalid number format in *10^ notation")
        else:
            try:
                return float(s) 
            except ValueError:
                raise ValueError("Invalid number format")

    # MAIN
    to = input("Enter the prefix of the unit to translate to: ").strip().title()
    origin = input("Enter the prefix of the unit you are translating from: ").strip().title()
    val_str = input("Enter the number fully (supports 1e6 or 1*10^6): ").strip()

    try:
        val = parse_number(val_str)
    except ValueError as e:
        print(e)
        exit()

    converted = doConver(origin, to, val)
    print(f"{val} {origin} = {converted} {to}")

run()