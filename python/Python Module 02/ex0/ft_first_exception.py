def input_temperature(temp_str) -> int:
    return int(temp_str)


def test_temperature():
    print("=== Garden temperature ===")
    print()
    print("Input data is '25'")
    try:
        result = input_temperature('25')
        print(f"Temperature is {result}")
    except ValueError:
        print(
            "Caught input_temperature error: invalid literal for int()"
            "with base 10:'25'"
            )
    print()

    print("Input data is 'abc'")
    try:
        result = input_temperature('abc')
        print(f"Temperature is {result}")
    except ValueError:
        print(
            "Caught input_temperature error: invalid literal for int()"
            "with base 10:'abc'"
            )
    print()
    print("All tests completed - program didn't crash!")


def ft_first_exception():
    test_temperature()


if __name__ == "__main__":
    ft_first_exception()
