import random

words = ['python', 'java', 'javascript', 'php']
print("HANGMAN")
word = random.choice(words)
guess = input(f"Guess the word {word[:3] + '-' * (len(word) - 3)}: > ")
if guess == word:
    print("You survived!")
else:
    print("You lost!")
