class Plant():
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = height
        self._age = age
        self._stats = Plant.Stats()

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        elif height >= 0:
            self._height = height
            print(f"Height updated: {self._height}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        elif age >= 0:
            self._age = age
            print(f"Age updated: {self._age} days")

    def show(self) -> None:
        self._stats._show_count += 1
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    @staticmethod
    def is_older_than_age(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    class Stats:
        def __init__(self) -> None:
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

        def display(self) -> None:
            print(
                f"Stats: {self._grow_count} grow, {self._age_count} age,"
                f" {self._show_count} show"
                )


def display_stats(plant: Plant) -> None:
    plant._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloomed = False

    def bloom(self) -> None:
        self._bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._bloomed is True:
            print(f"{self._name} is blooming beautifully!")
        elif self._bloomed is False:
            print(f"{self._name} has not bloomed yet")

    def grow(self) -> None:
        self._stats._grow_count += 1
        self._height = round(self._height + 8.0, 1)


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade_count} shade")

    def __init__(
            self, name: str, height: float,
            age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self._stats: Tree.Stats = Tree.Stats()
        self._trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        self._stats._shade_count += 1
        print(
            f"Tree {self._name} now produces a shade of {self._height}cm long"
            f" and {self._trunk_diameter}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self._trunk_diameter}cm")


class Vegetable(Plant):
    def __init__(
            self, name: str, height: float,
            age: int, harvest_season: str
    ) -> None:
        super().__init__(name, height, age)
        self._harvest_season = harvest_season
        self._nutritional_value = 0

    def grow(self) -> None:
        self._stats._grow_count += 1
        self._height = round(self._height + 2.1, 1)

    def age(self) -> None:
        self._stats._age_count += 1
        self._age += 1
        self._nutritional_value += 1

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        self._seed_count = 0

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seed_count}")

    def grow(self) -> None:
        self._stats._grow_count += 1
        self._height = round(self._height + 30, 1)

    def age(self) -> None:
        self._stats._age_count += 1
        self._age += 20

    def bloom(self) -> None:
        super().bloom()
        self._seed_count = 42


def ft_garden_analytics() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days older than a year? -> {Plant.is_older_than_age(30)}")
    print(f"Is 400 days older than a year? -> {Plant.is_older_than_age(400)}")
    print()

    rose = Flower("Rose", 15.0, 10, "red")
    print("=== Flower")
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    print("[statistics for Rose]")
    display_stats(rose)
    print()

    oak = Tree("Oak", 200.0, 365, 5.0)
    print("=== Tree")
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("[statistics for Oak]")
    display_stats(oak)
    print()

    seed = Seed("Sunflower", 80.0, 45, "yellow")
    print("=== Seed")
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.grow()
    seed.age()
    seed.bloom()
    seed.show()
    print("[statistics for Sunflower]")
    display_stats(seed)
    print()

    anonymous = Plant.create_anonymous()
    print("=== Anonymous")
    anonymous.show()
    print("[statistics for Unknown plant]")
    display_stats(anonymous)


if __name__ == "__main__":
    ft_garden_analytics()
