def whisper_cipher(text: str, shift: int) -> str:
    result = ""
    for ch in text:
        if "A" <= ch <= "Z":
            pos = (ord(ch) - ord("A") + shift) % 26
            result += chr(ord("A") + pos)
        elif "a" <= ch <= "z":
            pos = (ord(ch) - ord("a") + shift) % 26
            result += chr(ord("a") + pos)
        else:
            result += ch
    return result


def main() -> None:
    print(whisper_cipher("abc", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("Hello, World!", 3))
    print(whisper_cipher("abc", -1))
    print(whisper_cipher("abc", 27))
    print(whisper_cipher("ABC", 0))


main()
