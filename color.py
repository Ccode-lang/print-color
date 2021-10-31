def cprint(text, color):
    if color == "black":
        code = "\033[1;30m"
    elif color == "red":
        code = "\033[1;31m"
    elif color = "green":
        code = "\033[1;32m"
    elif color = "yellow":
        code = "\033[1;33m"
    elif color = "blue":
        code = "\033[1;34m"
    elif color = "magenta":
        code = "\033[1;35m"
    elif color = "cyan":
        code = "\033[1;36m"
    elif color = "white":
        code = "\033[1;37m"
    else:
        raise Exception("unknown color")
    print(code + text + "\033[1;0m")
