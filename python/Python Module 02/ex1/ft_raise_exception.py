def input_temperature(temp_str) -> int:
    temp = int(temp_str)
    if temp > 40:
        raise ValueError(f"{temp}° is too hot for plant (max 40°C)")
    elif temp < 0:
        raise ValueError(f"{temp}° is too cold for plants (min 0°C)")
    return temp


def test_temperature():
    print("=== Garden temperature Checker ===")
    print()
    print("Input data is '25'")
    try:
        result = input_temperature('25')
        print(f"Temperature is {result}")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()

    print("Input data is 'abc'")
    try:
        result = input_temperature('abc')
        print(f"Temperature is {result}")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()

    print("Input data is '100'")
    try:
        result = input_temperature('100')
        print(f"Temperature is {result}")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")
    print()

    print("Input data is '-50'")
    try:
        result = input_temperature('-50')
        print(f"Temperature is {result}")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")

    print("All tests completed - program didn't crash!")


def ft_raise_exception():
    test_temperature()


if __name__ == "__main__":
    ft_raise_exception()
