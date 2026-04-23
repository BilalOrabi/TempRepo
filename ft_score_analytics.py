import sys


def header(Title: str) -> None:
    print(Title)


def main() -> None:

    header("=== Player Score Analytics ===")

    args = sys.argv[1:]
    scores = []

    for arg in args:
        try:
            score = int(arg)
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{arg}'")

    if not scores:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return

    total_players = len(scores)
    total_scores = sum(scores)
    average_scores = total_scores / total_players
    high_score = max(scores)
    low_score = min(scores)
    range = high_score - low_score

    print(f"Total players: {total_players}")
    print(f"Total score: {total_scores}")
    print(f"Average score: {average_scores}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {range}")


if __name__ == "__main__":
    main()
