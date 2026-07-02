def string_permutation_checker(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False
    count: dict[str, int] = {}
    for ch in s1:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    for ch in s2:
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] < 0:
            return False
    return True


def main() -> None:
    print(string_permutation_checker("abc", "cab"))
    print(string_permutation_checker("abc", "ABC"))
    print(string_permutation_checker("ab c", "abc "))
    print(string_permutation_checker("ab c", "abc"))
    print(string_permutation_checker("a!b", "b!a"))
    print(string_permutation_checker("", ""))


main()
