import random


class Player:
    def __init__(self, name, achievements):
        self.name = name
        self.achievements = set(achievements)


def gen_player_achievements():
    all_achievements = [
        "First Kill", "Level 10", "Treasure Hunter",
        "Speed Demon", "Boss Slayer",
        "Collector", "Perfectionist",
        "Explorer", "Master Miner", "Puzzle Solver"
    ]

    number = random.randint(1, len(all_achievements))
    return set(random.sample(all_achievements, number))


def ft_achievement_tracker():
    print("=== Achievement Tracker System ===")
    print()
    players = [
        Player("Alice", gen_player_achievements()),
        Player("Charlie", gen_player_achievements()),
        Player("Bob", gen_player_achievements()),
        Player("David", gen_player_achievements())
    ]

    for player in players:
        print(f"Player {player.name}: {player.achievements}")
    print()

    all_achievements = set()
    for player in players:
        all_achievements = all_achievements.union(player.achievements)

    print("All distinct achievements:", all_achievements)
    print()

    common = players[0].achievements
    for player in players[1:]:
        common = common.intersection(player.achievements)

    print("Common achievements:", common)
    print()

    for player in players:
        others = set()

        for p in players:
            if p != player:
                others = others.union(p.achievements)

        unique = player.achievements.difference(others)
        missing = all_achievements.difference(player.achievements)

        print(f"Only {player.name} has: {unique}")
        print(f"{player.name} is missing:", missing)
        print()


if __name__ == "__main__":
    ft_achievement_tracker()
