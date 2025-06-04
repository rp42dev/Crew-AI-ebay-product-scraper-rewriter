# utils/terminal_style.py

from colorama import Fore, Style

def style_text(text, color=None, bold=False):
    colors = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "yellow": Fore.YELLOW,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "white": Fore.WHITE,
    }

    styled = ""
    if bold:
        styled += Style.BRIGHT
    if color in colors:
        styled += colors[color]
    styled += text + Style.RESET_ALL
    return styled
