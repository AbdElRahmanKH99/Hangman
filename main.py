import random
words = ["good", "bad", "ugly"]
correct_word = random.choice(words)
spaces = ["_"] * len(correct_word)
tries = 6
guessed_letters = []
hangman_pics = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
      |
      |
      |
      |
      |
=========''']

print("Welcome to Hangman Game!")
input("Press Enter to generate a word...")
print("Guess this word:")
print(" ".join(spaces))
print(hangman_pics[7])

while "_" in spaces and tries > 0:
    guessed = input("Please guess a letter: ").lower()

    if guessed in guessed_letters:
        print("You already guessed that. Try again.")
        print(f"You have {tries} more tries")
        continue

    if guessed not in correct_word:
        tries -= 1
        print(hangman_pics[tries])
    else:
      for position in range(len(correct_word)):
          if correct_word[position] == guessed:
              spaces[position] = guessed

    print(" ".join(spaces))
    print(f"You have {tries} more tries")
    guessed_letters.append(guessed)

if tries > 0:
    print("[","".join(spaces),"]")
    print("""
        *******
        You Win
        *******
""")
else:
    print("\n           You lose!")
    # print(hangman_pics[tries])