def _():
    from helpers.pyon import pyon
    from helpers import callconversions as cc
    from helpers import colors
    element = input("Enter the element abbreviation or atomic number: ").strip().lower()

    # Determine if input is a number
    if element.isnumeric():
        elementsy = atomicNumToSymbol[element]
    else:
        elementsy = element.capitalize()

    try:
        props = mapping[elementsy.lower()]
    except KeyError:
        # Try nameToSymbol lookup
        try:
            elementsy = nameToSymbol[element].lower()
            props = mapping[elementsy]
        except KeyError:
            print(f"Error: element '{element}' not found. Exiting...")
            sys.exit(0)

    # Unpack properties safely
    try:
        (name, weight, prop, atomicNum, electronegativity, oxidationStates,
         ionizationEnergy, atomicRadius, density, meltingPoint, boilingPoint) = props
    except ValueError:
        # Handle extra properties like safetyRating, safetyReason
        (name, weight, prop, atomicNum, electronegativity, oxidationStates,
         ionizationEnergy, atomicRadius, density, meltingPoint, boilingPoint,
         safetyRating, safetyReason) = props

    if safetyRating.lower() == "very high":
        safetyRating = veryHigh + safetyRating + endc
    elif safetyRating.lower() == "high":
        safetyRating = high + safetyRating + endc
    elif safetyRating.lower() == "moderate": 
        safetyRating = moderate + safetyRating + endc
    elif safetyRating.lower() == "low":
        safetyRating = low + safetyRating + endc

    #Ion status
    typ = input("Is the Ion a Cation (Positively charged) or Anion (Negatively charged)?: ")
    charge = int(input("Enter the charge in a '1 / 2' format: "))

    if typ.lower() == "cation":
        if charge > 0:
            charge = int(f"-{charge}")
    
    protons = atomicNum
    neutrons = round(weight - protons)
    electrons = protons + charge
    print(
        f"""
        Basic Info:
            Symbol: {elementsy}
            Name: {name}
            Weight: {weight}
            Property: {prop}
            Atomic Number: {atomicNum}

        Subatomic Particles Count:
            protons: {protons}
            neutrons: {neutrons}
            electrons: {electrons}

        Advanced Info:

            Electronegativity: {electronegativity}
            Oxidization Status: {oxidationStates} 
            Ionization Energy: {ionizationEnergy}
            Atomic Radius: {atomicRadius} 
            Density: {density}
            Melting Point: {meltingPoint} 
            Boiling Point: {boilingPoint}

        Safety:

            safety Rating: {safetyRating}
            safety Reason: {safetyReason}
        """
    )

    choice = input("Show Bohr model animation? (y/n): ").lower().strip()
    if choice == "y":
        bohr_animation_auto(element, atomicNum, electrons)