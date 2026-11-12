def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    try:
        temp_int = int(temp_str)
        print(f"Temperature is now {temp_int}°C\n")
        return temp_int
    except ValueError as e:
        print(f"Caught input_temperature error: {e}\n")


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    input_temperature("25")
    input_temperature("abc")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
