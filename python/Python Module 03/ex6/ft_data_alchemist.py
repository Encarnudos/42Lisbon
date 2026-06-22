import random


def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===")
    names = [
        "Alice", "bob", "Charlie", "dylan",
        "Emma", "Gregory", "john", "kevin", "Liam"
    ]
    print(f"Initial list of players: {names}")
    result = [name.capitalize() for name in names]
    print(f"New list with all names capitalized: {result}")
    already_capitalized = [name for name in names if name.istitle()]
    print(f"New list of capitalized names only: {already_capitalized}")
    score_dict = {name: random.randint(0, 1000) for name in result}
    print(f"Score dict: {score_dict}")
    average = round(sum(score_dict.values()) / len(score_dict), 2)
    print(f"Score average is {average}")
    high_scores = {
        name: score for name, score in
        score_dict.items() if score > average
    }
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
