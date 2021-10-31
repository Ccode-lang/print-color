def cprint(text, color):
    print(f"\033[1;{color}" + text + "\033[1;0m")
