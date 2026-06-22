import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = [
        "run", "eat", "sleep", "grab",
        "move", "climb", "swim", "release"
    ]

    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_events(
        events:
        list[tuple[str, str]]) -> typing.Generator[
            tuple[str, str], None, None
        ]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    for i in range(1000):
        event = next(event_gen)
        name, action = event
        print(f"Event {i}: Player {name} did action {action}")
    event_list = []
    for _ in range(10):
        event_list.append(next(event_gen))
        print(f"Built list of 10 events: {event_list}")
    for event in consume_events(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    ft_data_stream()
