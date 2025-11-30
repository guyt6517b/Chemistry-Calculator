print(
    """
    The Scientific Calculator: Public Disribution (SIC:PD)
    (c) 2025 Guyt6517
    Educational use only. Not for resale without permission.

    Some portions of code were generated with assistance from AI tools
    """
)

print(
    """
    NAME: \t Updates \t\t\t CALL: \t 0

    NAME: \t Read Me \t\t\t CALL: \t 1

    NAME: \t Metric - Metric conversions \t CALL: \t 2

    NAME: \t Temperature Conversions \t CALL: \t 3

    NAME: \t Pressure Conversions \t\t CALL: \t 4

    NAME: \t Periodic Table \t\t CALL: \t 5

    NAME: \t Imperial - Metric Conversions \t CALL: \t 6

    NAME: \t pH Scale Calculator \t\t CALL: \t 7
    """
)
call = input("Enter a call: ")

if call == "0":
    o = open("terminal/updates.txt", "r")
    o = o.read()
    print(o)


elif call == "1":
    o = open("terminal/readme.md", "r")
    o = o.read()
    print(o)

elif call == "2":
    from operations import mmuc
elif call == "3":
    from operations import tc
elif call == "4":
    from operations import puc
elif call == "5":
    from operations import pt
elif call == "6":
    from operations import im
elif call == "7":
    from operations import phscale