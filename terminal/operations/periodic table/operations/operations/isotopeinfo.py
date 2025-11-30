def isotope():
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
    nuclideNotation = int(input(f"Enter the Nuclide Notation / Mass number(-6, 6 being notation): "))

    if safetyRating.lower() == "very high":
        safetyRating = veryHigh + safetyRating + endc
    elif safetyRating.lower() == "high":
        safetyRating = high + safetyRating + endc
    elif safetyRating.lower() == "moderate": 
        safetyRating = moderate + safetyRating + endc
    elif safetyRating.lower() == "low":
        safetyRating = low + safetyRating + endc

    protons = atomicNum
    if protons <= nuclideNotation:
        neutrons = round(nuclideNotation - protons)
    else:
        neutrons = "Nan"

    typ = input("Is the Ion a Cation (Positively charged) or Anion (Negatively charged) or is it neutral (No charge): ")
    if typ.lower() != "neutral":
        charge = int(input("Enter the charge in a '1 / 2' format: "))

        if typ.lower() == "cation":
            if charge > 0:
                charge = int(f"-{charge}")
        electrons = protons + charge
    else:
        electrons = protons


    if atomicNum >= 1 and atomicNum <= 20:
        cat = "light"
    elif atomicNum >= 21 and atomicNum <= 82:
        cat = "medium"
    else:
        cat = "heavy"



    #below code was fixed with GenAi

    if cat == "light":
        if abs(neutrons - protons) <= 1:
            stableStatus = "stable"
        else:
            stableStatus = "unstable"
    elif cat == "medium":
        if neutrons >= protons:
            stableStatus = "stable"
        else:
            stableStatus = "unstable"
    else: # heavy
        if float(neutrons) > 1.5 * float(protons):
            stableStatus = "unstable"
        else:
            stableStatus = "stable"

    import periodictable

    abundance = getattr(periodictable, elementsy.capitalize())
    abundace = float(abundance[nuclideNotation].abundance)

    
    #abundance = "disabled"
    if abundance == 0:
        stableStatus = "unstable"
    else:
        stableStatus = "stable"
    abundance = str(abundance * 100)[0:4] + "%"

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