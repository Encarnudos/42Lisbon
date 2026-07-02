def is_letter(ch: str) -> bool:
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def to_lower(ch: str) -> str:
    if "A" <= ch <= "Z":
        return chr(ord(ch) + 32)
    return ch


def echo_validator(text: str) -> bool:
    cleaned = ""
    for ch in text:
        if is_letter(ch):
            cleaned += to_lower(ch)
    i = 0
    j = len(cleaned) - 1
    while i < j:
        if cleaned[i] != cleaned[j]:
            return False
        i += 1
        j -= 1
    return True


def main() -> None:
    print(echo_validator("A man a plan a canal Panama"))
    print(echo_validator("Never odd or even"))
    print(echo_validator("hello"))
    print(echo_validator("Ana"))
    print(echo_validator(""))
    print(echo_validator("12321"))


main()
