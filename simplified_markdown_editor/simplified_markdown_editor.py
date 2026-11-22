FORMATTERS = (
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line",
)


def print_help():
    print("Available formatters: " + " ".join(FORMATTERS))
    print("Special commands: !help !done")


def format_header():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            level = 0
        if 1 <= level <= 6:
            break
        print("The level should be within the range of 1 to 6")
    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def format_list(ordered):
    while True:
        try:
            rows = int(input("Number of rows: "))
        except ValueError:
            rows = 0
        if rows > 0:
            break
        print("The number of rows should be greater than zero")

    lines = []
    for i in range(1, rows + 1):
        row_text = input(f"Row #{i}: ")
        prefix = f"{i}." if ordered else "*"
        lines.append(f"{prefix} {row_text}\n")
    return "".join(lines)


def apply_formatter(fmt):
    if fmt == "plain":
        return input("Text: ")
    if fmt == "bold":
        return f"**{input('Text: ')}**"
    if fmt == "italic":
        return f"*{input('Text: ')}*"
    if fmt == "inline-code":
        return f"`{input('Text: ')}`"
    if fmt == "link":
        label = input("Label: ")
        url = input("URL: ")
        return f"[{label}]({url})"
    if fmt == "header":
        return format_header()
    if fmt == "ordered-list":
        return format_list(ordered=True)
    if fmt == "unordered-list":
        return format_list(ordered=False)
    if fmt == "new-line":
        return "\n"
    return ""


def main():
    buffer = []
    while True:
        choice = input("Choose a formatter: ").strip()
        if choice == "!help":
            print_help()
        elif choice == "!done":
            with open("output.md", "w", encoding="utf-8") as f:
                f.write("".join(buffer))
            break
        elif choice in FORMATTERS:
            buffer.append(apply_formatter(choice))
            print("".join(buffer))
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()
