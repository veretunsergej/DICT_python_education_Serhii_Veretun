WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def print_board(cells):
    print("---------")
    for row in range(3):
        line = " ".join(cells[row * 3:(row + 1) * 3])
        print(f"| {line} |")
    print("---------")


def check_winner(cells, symbol):
    return any(cells[a] == cells[b] == cells[c] == symbol for a, b, c in WIN_LINES)


def main():
    cells = [" "] * 9
    print_board(cells)
    turn = "X"

    while True:
        coords = input("Enter the coordinates: ").split()
        if len(coords) != 2:
            print("You should enter numbers!")
            continue
        try:
            row, col = int(coords[0]), int(coords[1])
        except ValueError:
            print("You should enter numbers!")
            continue

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        idx = (row - 1) * 3 + (col - 1)
        if cells[idx] != " ":
            print("This cell is occupied! Choose another one!")
            continue

        cells[idx] = turn
        print_board(cells)

        if check_winner(cells, turn):
            print(f"{turn} wins")
            break
        if " " not in cells:
            print("Draw")
            break

        turn = "O" if turn == "X" else "X"


if __name__ == "__main__":
    main()
