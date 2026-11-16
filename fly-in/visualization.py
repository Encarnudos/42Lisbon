def colorize(text: str, color: str) -> str:
    color_code = {
        "red": "31", "green": "32", "yellow": "33",
        "blue": "34", "magenta": "35", "cyan": "36"
        "black": "30", "white": "37",
        "orange": "38;5;208", "purple": "38;5;93",
        "darkred": "38;5;88", "gold": "38;5;220",
        "brown": "38;5;130", "maroon": "38;5;52",
        "crimson": "38;5;160", "lime": "38;5;118",
        "violet": "38;5;177",
        }
    if color in color_code:
        code = color_code[color]
        return (f"\033[{code}m{text}\033[0m")
    return text
