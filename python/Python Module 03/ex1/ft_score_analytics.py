import sys


def ft_score_analytics():
    print("=== Player Score Analytics ===")
    scores = []
    for value in sys.argv[1:]:
        try:
            scores.append(int(value))
        except ValueError:
            print(f"Invalid parameter:'{value}'")
    if len(scores) == 0:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        x = sum(scores) / len(scores)
        print(f"Average score: {x}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    ft_score_analytics()
