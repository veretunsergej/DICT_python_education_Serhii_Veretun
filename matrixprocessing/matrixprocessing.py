def parse_number(token):
    return float(token) if "." in token else int(token)


def read_matrix(size_prompt="Enter matrix size: ", matrix_prompt="Enter matrix:"):
    rows, cols = map(int, input(size_prompt).split())
    print(matrix_prompt)
    matrix = []
    for _ in range(rows):
        row = [parse_number(x) for x in input().split()]
        matrix.append(row)
    return rows, cols, matrix


def format_val(val):
    if isinstance(val, int):
        return str(val)
    if abs(val - round(val)) < 1e-9:
        return str(int(round(val)))
    return str(round(val, 4))


def print_matrix(matrix, fixed_2dec=False):
    print("The result is:")
    for row in matrix:
        if fixed_2dec:
            print(" ".join(f"{(0.0 if abs(x) < 1e-9 else x):.2f}" for x in row))
        else:
            print(" ".join(format_val(x) for x in row))


def add_matrices():
    r1, c1, m1 = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
    r2, c2, m2 = read_matrix("Enter size of second matrix: ", "Enter second matrix:")
    if r1 != r2 or c1 != c2:
        print("The operation cannot be performed.")
        return
    res = [[m1[i][j] + m2[i][j] for j in range(c1)] for i in range(r1)]
    print_matrix(res)


def multiply_by_constant():
    r, c, m = read_matrix("Enter size of matrix: ", "Enter matrix:")
    const = parse_number(input("Enter constant: "))
    res = [[m[i][j] * const for j in range(c)] for i in range(r)]
    print_matrix(res)


def multiply_matrices():
    r1, c1, m1 = read_matrix("Enter size of first matrix: ", "Enter first matrix:")
    r2, c2, m2 = read_matrix("Enter size of second matrix: ", "Enter second matrix:")
    if c1 != r2:
        print("The operation cannot be performed.")
        return
    res = [[sum(m1[i][k] * m2[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]
    print_matrix(res)


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    choice = input("Your choice: ").strip()
    r, c, m = read_matrix("Enter matrix size: ", "Enter matrix:")

    if choice == "1":
        res = [[m[j][i] for j in range(r)] for i in range(c)]
    elif choice == "2":
        res = [[m[r - 1 - j][c - 1 - i] for j in range(r)] for i in range(c)]
    elif choice == "3":
        res = [row[::-1] for row in m]
    elif choice == "4":
        res = m[::-1]
    else:
        print("The operation cannot be performed.")
        return
    print_matrix(res)


def minor_matrix(matrix, row, col):
    return [
        [matrix[i][j] for j in range(len(matrix)) if j != col]
        for i in range(len(matrix)) if i != row
    ]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    total = 0
    for col in range(n):
        sign = -1 if col % 2 else 1
        total += sign * matrix[0][col] * determinant(minor_matrix(matrix, 0, col))
    return total


def calculate_determinant():
    r, c, m = read_matrix("Enter matrix size: ", "Enter matrix:")
    if r != c:
        print("The operation cannot be performed.")
        return
    det = determinant(m)
    print("The result is:")
    print(format_val(det))


def inverse_matrix():
    r, c, m = read_matrix("Enter matrix size: ", "Enter matrix:")
    if r != c:
        print("The operation cannot be performed.")
        return
    det = determinant(m)
    if abs(det) < 1e-12:
        print("This matrix doesn't have an inverse.")
        return
    n = r
    if n == 1:
        inv = [[1.0 / det]]
    else:
        cofactors = []
        for i in range(n):
            row = []
            for j in range(n):
                sign = -1 if (i + j) % 2 else 1
                row.append(sign * determinant(minor_matrix(m, i, j)))
            cofactors.append(row)
        inv = [[cofactors[j][i] / det for j in range(n)] for i in range(n)]
    print_matrix(inv, fixed_2dec=True)


def main():
    while True:
        print("1. Add matrices")
        print("2. Multiply matrix by a constant")
        print("3. Multiply matrices")
        print("4. Transpose matrix")
        print("5. Calculate a determinant")
        print("6. Inverse matrix")
        print("0. Exit")
        choice = input("Your choice: ").strip()
        if choice == "1":
            add_matrices()
        elif choice == "2":
            multiply_by_constant()
        elif choice == "3":
            multiply_matrices()
        elif choice == "4":
            transpose_matrix()
        elif choice == "5":
            calculate_determinant()
        elif choice == "6":
            inverse_matrix()
        elif choice == "0":
            break


if __name__ == "__main__":
    main()
