def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    resultado = []
    for row in matrix:
        new_line = []
        for i in range(len(row) - 1, -1, -1):
            new_line.append(row[i])
        resultado.append(new_line)
    return resultado


def main() -> None:
    original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mirrored = mirror_matrix(original)
    print("mirrored:", mirrored)
    print("original:", original, "(intacta)")
    print(mirror_matrix([[1], [2, 3], []]))
    print(mirror_matrix([]))


main()
