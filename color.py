def cprint(text, color):
    print(f"\033[1;" + str(color) + " " + text + "\033[1;0m")
