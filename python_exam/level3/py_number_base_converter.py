def digit_value(ch: str) -> int:
    if "0" <= ch <= "9":
        return ord(ch) - ord("0")
    if "A" <= ch <= "Z":
        return ord(ch) - ord("A") + 10
    return -1


def value_to_digit(v: int) -> str:
    if v < 10:
        return chr(ord("0") + v)
    return chr(ord("A") + v - 10)


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"
    if number == "":
        return "ERROR"
    value = 0
    for ch in number:
        d = digit_value(ch)
        if d == -1 or d >= from_base:
            return "ERROR"
        value = value * from_base + d
    if value == 0:
        return "0"
    result = ""
    while value > 0:
        result = value_to_digit(value % to_base) + result
        value //= to_base
    return result


def main() -> None:
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("1010", 2, 10))
    print(number_base_converter("Z", 36, 10))
    print(number_base_converter("0", 10, 2))
    print(number_base_converter("G", 16, 10))
    print(number_base_converter("123", 1, 10))
    print(number_base_converter("10", 2, 40))
    print(number_base_converter("12", 2, 10))
    print(number_base_converter("", 10, 2))


main()
