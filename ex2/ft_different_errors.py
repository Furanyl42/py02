def garden_operations(operation_number: int) -> None:
    match operation_number:
        case 0:
            int("abc")
        case 1:
            _ = 1 / 0
        case 2:
            open("doesntexist.txt")
        case 3:
            _ = "abc" + 2
        case _:
            pass


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===\n")
    input_temperature("25")
    input_temperature("abc")
    input_temperature("100")
    input_temperature("-50")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
