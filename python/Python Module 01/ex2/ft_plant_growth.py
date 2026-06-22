class Plant():
    name: str = ""
    height: float = 0.0
    _age: int = 0

    def grow(self) -> None:
        self.height = round(self.height + 0.8, 1)

    def age(self) -> None:
        self._age += 1


def ft_plant_growth() -> None:
    rose = Plant()
    rose.name = "Rose"
    rose.height = 25.0
    rose._age = 30

    print("=== Garden Plant Growth ===")
    print(f"{rose.name}: {rose.height}cm, {rose._age} days old")

    start_height = rose.height

    for day in range(1, 8):
        rose.grow()
        rose.age()
        print(f"=== Day {day} ===")
        print(f"{rose.name}: {rose.height}cm, {rose._age} days old")

    total_growth = round(rose.height - start_height, 1)
    print(f"Growth this week: {total_growth}cm")


if __name__ == "__main__":
    ft_plant_growth()
