"""The ph scale measures how acidic or basic a substance is based on its concentration of hydrogen ions
ranges from 0 to 14"""

"""pH = -log₁₀[H⁺]"""

acidic = '\033[91m' #Red
slightlyAcidic = '\033[93m' #Yellow
neutral = '\033[92m' #Green
slightlyAlkali = '\033[94m' # Blue
alkali = '\033[95m' #Purple

ENDC = '\033[0m' #resets color

import math

h = input("Enter the molar concentration of hydrogen ions in the solution: ")

if h.find("^") != -1:
    h = h.replace("^", "**")

    h = h.replace(" ", "")

    hExpo = h.split("**")[1]
    hFront = h.split("*")[0]
    hBack = h.split("*")[1]



    h = float(hFront) * float(hBack) ** float(hExpo)
    pH = round(-(math.log(h, 10)), 2)


elif h.find("pH") != -1:
    h = h.replace("pH", "")
    pH = float(h)
else:
    h = float(h)
    pH = round(-(math.log(h, 10)), 2)

if 0 < pH and pH < 6:
    print("The pH value:", str(pH) + " is " + acidic + " acidic " + ENDC)

elif 6 < pH and pH < 7:
    print("The pH value:", str(pH) + " is " + slightlyAcidic + "slightly acidic" + ENDC) 

elif pH <= 7 and pH <= 7.5:
    print("The pH value:", str(pH) + " is " + neutral + " neutral" + ENDC)

elif 7.5 < pH and pH < 10:
    print("The pH value:", str(pH) + " is " + slightlyAlkali + "slightly alkali" + ENDC)

elif 10 < pH and pH < 14:
    print("The pH value:", str(pH) + " is " + alkali + "alkali" + ENDC)

else:
    raise ValueError(f"the pH value {pH} is out of the 14 range")

#mapping = {
#    "0":("acidic like battery acid.")
#    "1":("acidic like stomach acid.")
#    "2":("acidic like lemon juice, vinegar")
#    "2.5":("acidic like carbonated beverages")
#    "3":("acidic like grapefruit and orange juice")
#}