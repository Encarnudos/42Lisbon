def is_letter(ch: str) -> bool:
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def to_lower(ch: str) -> str:
    if "A" <= ch <= "Z":
        return chr(ord(ch) + 32)
    return ch


def to_upper(ch: str) -> str:
    if "a" <= ch <= "z":
        return chr(ord(ch) - 32)
    return ch


def string_sculptor(text: str) -> str:
    result = ""
    lower = True
    for ch in text:
        if ch == " ":
            result += ch
            lower = True
        elif is_letter(ch):
            if lower:
                result += to_lower(ch)
            else:
                result += to_upper(ch)
            lower = not lower
        else:
            result += ch
    return result


def main() -> None:
    print(string_sculptor("hello world"))
    print(string_sculptor("Abc123def"))
    print(string_sculptor("a b"))
    print(string_sculptor("a,b"))
    print(string_sculptor(""))


main()
