def inter(s1: str, s2: str) -> str:
    resultado = ""
    for ch in s1:
        if ch in s2 and ch not in resultado:
            resultado += ch
    return resultado


def main() -> None:
    print(inter("hello", "world"))
    print(inter("aabbcc", "abc"))
    print(inter("abc", "xyz"))
    print(inter("", "abc"))
    print(inter("Hello", "hello"))


main()
