def is_digit(ch: str) -> bool:
    return "0" <= ch <= "9"


def pattern_tracker(text: str) -> int:
    total = 0
    for i in range(len(text) - 1):
        a = text[i]
        b = text[i + 1]
        if is_digit(a) and is_digit(b) and ord(b) - ord(a) == 1:
            total += 1
    return total


def main() -> None:
    print(pattern_tracker("12345"))
    print(pattern_tracker("9012"))
    print(pattern_tracker("112233"))
    print(pattern_tracker("899"))
    print(pattern_tracker("1a2b3"))
    print(pattern_tracker("753"))
    print(pattern_tracker(""))


main()
