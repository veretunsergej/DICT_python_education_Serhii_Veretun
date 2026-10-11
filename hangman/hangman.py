import random

words = ['python', 'java', 'javascript', 'php']

print("HANGMAN")

while True:
    menu = input('Type "play" to play the game, "exit" to quit: > ')
    if menu == "exit":
        break
    elif menu == "play":
        target = random.choice(words)
        target_set = set(target)
        guessed_letters = set()
        tries = 8
        print()

        while tries > 0:
            current_state = "".join([c if c in guessed_letters else "-" for c in target])
            print(current_state)

            if set(current_state) == target_set:
                print(f"You guessed the word {target}!")
                print("You survived!")
                break

            letter = input("Input a letter: > ")

            if len(letter) != 1:
                print("You should input a single letter")
                print()
                continue

            if not ('a' <= letter <= 'z'):
                print("Please enter a lowercase English letter")
                print()
                continue

            if letter in guessed_letters:
                print("You've already guessed this letter")
                print()
                continue

            guessed_letters.add(letter)

            if letter in target_set:
                if all(c in guessed_letters for c in target):
                    print(f"You guessed the word {target}!")
                    print("You survived!")
                    break
            else:
                print("That letter doesn't appear in the word")
                tries -= 1

            if tries == 0:
                print("You lost!")
                break
            print()
