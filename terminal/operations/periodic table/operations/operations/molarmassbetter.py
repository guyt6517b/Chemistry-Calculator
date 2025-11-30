from collections import defaultdict, Counter

class FormulaParser:
    def __init__(self, formula_str):
        self.formula = formula_str
        self.n = len(formula_str)
        self.i = 0
    
    def parse(self):
        """Main entry point for parsing the entire formula."""
        # Split off hydrate part (e.g., H2O*5)
        parts = self.formula.split('*')
        main_formula = parts[0]
        hydrate_multiplier = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 1

        # Parse the main part of the formula
        # We use a stack to handle nested parentheses (list of dictionaries/Counters)
        stack = [Counter()]
        self.i = 0 # Reset internal index for main parsing
        
        while self.i < len(main_formula):
            char = main_formula[self.i]

            if char.isupper():
                # Parse an element and its count
                element, count = self._parse_element_and_count(main_formula)
                stack[-1][element] += count
            
            elif char == '(':
                # Push a new Counter onto the stack to start a new group
                self.i += 1 # Consume the '('
                stack.append(Counter())
                
            elif char == ')':
                # Pop the just-finished group off the stack
                self.i += 1 # Consume the the ')'
                completed_group = stack.pop()
                
                # Parse the multiplier immediately following the ')'
                multiplier = self._parse_number(main_formula)
                
                # Apply the multiplier to the popped group and merge with the parent group
                parent_group = stack[-1]
                for elem, count in completed_group.items():
                    parent_group[elem] += count * multiplier
            
            else:
                # Skip invalid characters or whitespace
                self.i += 1

        # Apply the final hydrate multiplier
        final_counts = stack[0]
        for elem in final_counts:
            final_counts[elem] *= hydrate_multiplier
            
        return dict(final_counts) # Return as a standard dictionary

    def _parse_element_and_count(self, s):
        """Helper to extract an element symbol and its subscript count."""
        start = self.i
        # Element must start with uppercase, potentially followed by lowercase
        self.i += 1 
        if self.i < len(s) and s[self.i].islower():
            self.i += 1
        element = s[start:self.i]
        
        count = self._parse_number(s)
        
        return element, count

    def _parse_number(self, s):
        """Helper to extract a multiplier number."""
        start = self.i
        while self.i < len(s) and s[self.i].isdigit():
            self.i += 1
        
        number_str = s[start:self.i]
        return int(number_str) if number_str else 1


def calculate_molar_mass(element_counts, mapping_data):
    """
    Calculates the total molar mass from element counts and atomic weight data.
    """
    total_molar_mass = 0.0
    errors = []

    for element, count in element_counts.items():
        element_key = element.lower() # Mapping keys usually lowercased
        if element_key in mapping_data:
            # Assuming mapping structure is (atomic_number, weight, ...)
            _, weight, *__ = mapping_data[element_key]
            total_molar_mass += weight * count
        else:
            errors.append(element)
    
    if errors:
        print(f"Warning: Could not find atomic weight data for elements: {', '.join(errors)}")
        return None, errors
    
    return round(total_molar_mass, 4), errors

# --- Example Usage (Integration with existing script logic) ---

# Load mapping data first (simulated data for demonstration)
# Replace this with your actual 'atom data table.pyon' loading logic
from helpers.pyon import pyon 
mapping = pyon.run("/home/karel/terminal/operations/periodic table/atom data table.pyon")


if mapping is not None:
    # Example formulas: H2O*5, (NH4)2Cr2O7, Al2(SO4)3
    formula_input = input("Enter the formula (e.g., H2O*5 or (NH4)2Cr2O7): ")
    
    # Use the new parser class
    parser = FormulaParser(formula_input)
    element_counts = parser.parse()

    print(f"Input formula: {formula_input}")
    print(f"Parsed element counts: {element_counts}") 

    molar_mass, errors = calculate_molar_mass(element_counts, mapping)
    
    if molar_mass is not None:
        print(f"Total Molar Mass: {molar_mass} g/mol")
        
        # --- Handle final calculations ---
        try:
            grams = float(input("Enter the number of grams: "))
            moles = float(input("Enter the number of moles: "))
            result = round(grams * molar_mass / moles, 2)
            print(f"There are {result} grams in {moles} of {formula_input}")
            result = round(grams * moles / molar_mass, 2)
            print(f"There are {result} moles in {grams} grams of {formula_input}")
        except ValueError:
            print("Invalid input for grams or moles.")