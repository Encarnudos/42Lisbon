def to_lower(s: str) -> str:
    if "A" <= s <= "Z":
        return chr(ord(s) + 32)
    return s


def normalize(s: str) -> str:
    resultado = ""
    for ch in s:
        resultado += to_lower(ch)
    return resultado


def count_vowels(s: str) -> int:
    total = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            total += 1
    return total


def should_swap(a: str, b: str) -> bool:
    if len(a) != len(b):
        return len(a) > len(b)

    na, nb = normalize(a), normalize(b)
    if na != nb:
        return na > nb

    if count_vowels(a) != count_vowels(b):
        return count_vowels(a) > count_vowels(b)

    return False


def cryptic_sorter(strings: list[str]) -> list[str]:
    n = len(strings)
    for i in range(n):
        for j in range(n - 1 - i):
            if should_swap(strings[j], strings[j + 1]):
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
    return strings


def main() -> None:
    print(cryptic_sorter(["Cat", "cat", "dog", "ox", "Dog"]))
    print(cryptic_sorter(["banana", "Apple", "kiwi", "fig", "cherry"]))
    print(cryptic_sorter([]))
    print(cryptic_sorter(["solo"]))


main()
