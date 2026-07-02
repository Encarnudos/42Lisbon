def twist_sequence(arr: list[int], k: int) -> list[int]:
    n = len(arr)
    if n == 0:
        return []
    k = k % n
    result = []
    for i in range(n - k, n):
        result.append(arr[i])
    for i in range(0, n - k):
        result.append(arr[i])
    return result


def main() -> None:
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    print(twist_sequence([1, 2, 3, 4, 5], 7))
    print(twist_sequence([1, 2, 3], 0))
    print(twist_sequence([1, 2, 3], 3))
    print(twist_sequence([], 4))
    print(twist_sequence([7], 5))


main()
