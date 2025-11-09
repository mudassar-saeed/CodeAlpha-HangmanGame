import random

# List of predefined words
words = ["inception", "avatar", "gladiator", "titanic", "interstellar"]

# Randomly select a word
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("_ " * len(secret_word))

# Loop until the game is over or win
while attempts_left > 0:
    guess = input("\nEnter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetic letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in secret_word:
        print("✅ Correct guess!")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}")

    # Display current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\n" + display_word)

    # Check if player has guessed all letters
    if all(letter in guessed_letters for letter in secret_word):
        print("\n🎉 Congratulations! You guessed the word correctly!")
        break
else:
    print(f"\n💀 Game Over! The word was '{secret_word}'. Better luck next time!")
