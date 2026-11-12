def input_temperature(temp_str: str) -> int:
    print(f"Input data is '{temp_str}'")
    temp_int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plants (max 40°C)")
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plants (min 0°C)")
    print(f"Temperature is now {temp_int}°C")
    return temp_int


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

    test_values = ["25", "abc", "100", "-50"]
    for val in test_values:
        try:
            input_temperature(val)
        except ValueError as e:
            print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")
    return


if __name__ == "__main__":
    test_temperature()
