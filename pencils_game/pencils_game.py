import random


def get_initial_pencils():
    print("How many pencils would you like to use:")
    while True:
        raw = input()
        if not raw.isdigit():
            print("The number of pencils should be numeric")
            continue
        count = int(raw)
        if count <= 0:
            print("The number of pencils should be positive")
            continue
        return count


def get_first_player():
    print("Who will be the first (John, Jack):")
    while True:
        name = input().strip()
        if name not in ("John", "Jack"):
            print("Choose between 'John' and 'Jack'")
            continue
        return name


def bot_move(pencils):
    if pencils == 1:
        return 1
    rem = (pencils - 1) % 4
    if rem == 0:
        return random.randint(1, 3)
    return rem


def human_move(pencils):
    while True:
        raw = input().strip()
        if raw not in ("1", "2", "3"):
            print("Possible values: '1', '2' or '3'")
            continue
        taken = int(raw)
        if taken > pencils:
            print("Too many pencils were taken")
            continue
        return taken


def main():
    pencils = get_initial_pencils()
    player = get_first_player()

    while pencils > 0:
        print("|" * pencils)
        if player == "Jack":
            print("Jack's turn:")
            taken = bot_move(pencils)
            print(taken)
        else:
            print("John's turn!")
            taken = human_move(pencils)

        pencils -= taken
        player = "Jack" if player == "John" else "John"

    print(f"{player} won!")


if __name__ == "__main__":
    main()
