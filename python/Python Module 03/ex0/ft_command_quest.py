import sys


def ft_command_quest():
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    arguments = len(sys.argv)
    x = 1
    if len(sys.argv) == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {arguments}")
        while x < arguments:
            print(f"Argument {x}: {sys.argv[x]}")
            x += 1
    print(f"Total arguments: {arguments}")


if __name__ == "__main__":
    ft_command_quest()
