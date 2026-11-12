class GardenError(Exception):
    def __init__(self, message: str = "Unkown Garden error") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Unkown Plant error") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Unkown Water error") -> None:
        super().__init__(message)


def check_plant(is_wilting: bool) -> None:
    if is_wilting:
        raise PlantError("The tomato plant is wilting!")


def check_water(enough_water: bool) -> None:
    if not enough_water:
        raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        check_plant(True)
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        check_water(False)
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        check_plant(True)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    try:
        check_water(False)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
