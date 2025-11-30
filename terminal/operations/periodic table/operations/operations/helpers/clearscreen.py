def clear_screen():
    time.sleep(.3)
    if os.name == "nt":
        os.system("cls")
    else:
        print("\033[H\033[J", end="")