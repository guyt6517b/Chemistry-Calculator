from helpers.pyon import pyon
mapping = pyon.run("/home/karel/terminal/operations/periodic table/atom data table.pyon")

formula = []
inp = ''

while inp != "stop":
    inp = input("Enter the next element (or stop)")
    if inp != "stop":
        if "*" in inp:
            loc = inp.find("*")
            subscript = int(inp[loc+1:])
            inp = inp[:loc]
            for _ in range(0, subscript):
                formula.append(inp.lower())
            
        else:
            formula.append(inp.lower())

elementMass = []

for item in formula:
    _, weight, _, _, _, _, _, _, _, _, _, _, _ = mapping[item]
    elementMass.append(weight)

print(round(sum(elementMass), 2), "g/mol")