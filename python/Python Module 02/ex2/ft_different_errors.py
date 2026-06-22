def garden_operations(operations_number) -> int:
    if operations_number == 0:
        return int("abc")
    elif operations_number == 1:
        return 10 / 0
    elif operations_number == 2:
        return open("missing_file.txt")
    elif operations_number == 3:
        return "text" + 5
    else:
        return None


def test_error_types():
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    try:
        garden_operations(0)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("Testing operations 1...")
    try:
        garden_operations(1)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("Testing operation 2...")
    try:
        garden_operations(2)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("Testing operation 3...")
    try:
        garden_operations(3)
    except TypeError as e:
        print(f"Caught TypeError: {e}")
    print("Testing operation 4...")
    try:
        garden_operations(4)
        print("Operation completed successfully")
    except Exception as e:
        print(e)
    print("Testing multiple error catch...")
    try:
        garden_operations(3)
    except (ValueError, TypeError) as e:
        print(f"Caught multiple-type handler: {e}")
    print()
    print("All error types tested successfully!")


def ft_different_errors():
    test_error_types()


if __name__ == "__main__":
    ft_different_errors()
