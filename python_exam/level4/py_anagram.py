def is_letter(ch: str) -> bool:
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def to_lower(ch: str) -> str:
    if "A" <= ch <= "Z":
        return chr(ord(ch) + 32)
    return ch


def clean(s: str) -> str:
    resultado = ""
    for ch in s:
        if is_letter(ch):
            resultado += to_lower(ch)
    return resultado


def anagram(s1: str, s2: str) -> bool:
    a = clean(s1)
    b = clean(s2)
    if len(a) != len(b):
        return False
    count: dict[str, int] = {}
    for ch in a:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in b:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True


def main() -> None:
    print(anagram("listen", "silent"))
    print(anagram("Dormitory", "Dirty Room"))
    print(anagram("The eyes", "They see"))
    print(anagram("hello", "world"))
    print(anagram("abc", "ab"))
    print(anagram("a", "A"))
    print(anagram("", ""))


main()
