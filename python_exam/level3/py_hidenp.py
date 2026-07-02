def hidenp(small: str, big: str) -> bool:
    i = 0
    for ch in big:
        if i < len(small) and ch == small[i]:
            i += 1
    return i == len(small)


def main() -> None:
    print(hidenp("ace", "abcde"))
    print(hidenp("aec", "abcde"))
    print(hidenp("abc", "abc"))
    print(hidenp("abc", "ab"))
    print(hidenp("", "abcde"))
    print(hidenp("abc", "ABC"))


main()
