import sys
import typing


def ft_archive_creation() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f: typing.IO = open(sys.argv[1])
        result = f.read()
        print("---")
        print()
        print(f"{result}")
        print()
        print("---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")
        print()
        lines = result.split("\n")
        new_lines = [line + "#" for line in lines if line]
        transformed = "\n".join(new_lines)
        print("Transform data:")
        print("---")
        print()
        print(f"{transformed}")
        print()
        print("---")
        new_file_name = input("Enter new file name (or empty): ")
        if not new_file_name:
            print("Not saving data.")
        else:
            print(f"Saving data to '{new_file_name}'")
            out = open(new_file_name, "w")
            out.write(transformed)
            out.close()
            print(f"Data saved in file '{new_file_name}'.")
    except OSError as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")


if __name__ == "__main__":
    ft_archive_creation()
