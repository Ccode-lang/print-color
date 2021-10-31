def cprint(text, color):
    if color == "black":
        code = "\033[1;30m"
    elif color == "red":
        code = "\033[1;31m"
    print(code + text + "\033[1;0m")
