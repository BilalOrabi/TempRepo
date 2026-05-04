import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]

ACTIONS = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "use", "release"
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield random.choice(PLAYERS), random.choice(ACTIONS)


def consume_event(
    events: list[tuple[str, str]]
) -> Generator[tuple[str, str], None, None]:
    while events:
        yield events.pop(random.randrange(len(events)))


def main() -> None:
    print("=== Game Data Stream Processor ===")

    generator = gen_event()

    for i in range(1000):
        name, action = next(generator)
        print(f"Event {i}: Player {name} did action {action}")

    events_list = [next(generator) for _ in range(10)]
    print(f"Built list of 10 events: {events_list}")

    for event in consume_event(events_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events_list}")


if __name__ == "__main__":
    main()
