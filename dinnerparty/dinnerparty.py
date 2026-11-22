import random


def format_amount(value):
    rounded = round(value, 2)
    return int(rounded) if rounded.is_integer() else rounded


def main():
    print("Enter the number of friends joining (including you):")
    try:
        count = int(input())
    except ValueError:
        count = 0

    if count <= 0:
        print("No one is joining for the party")
        return

    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(count):
        name = input().strip()
        friends[name] = 0

    print("Enter the total amount:")
    total_amount = float(input())

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    choice = input().strip()

    if choice == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")
        if count > 1:
            share = format_amount(total_amount / (count - 1))
        else:
            share = 0
        for name in friends:
            friends[name] = 0 if name == lucky_one else share
    else:
        print("No one is going to be lucky")
        share = format_amount(total_amount / count)
        for name in friends:
            friends[name] = share

    print(friends)


if __name__ == "__main__":
    main()
