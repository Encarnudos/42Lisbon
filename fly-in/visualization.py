def colorize(text: str, color: str) -> str:
    color_code = {
        "red": "31", "green": "32", "yellow": "33",
        "blue": "34", "magenta": "35", "cyan": "36"
        }
    if color in color_code:
        code = color_code[color]
        return (f"\033[{code}m{text}\033[0m")
    return text
