import random

WORDS = ["python", "computer", "programming", "developer", "technology"]
MAX_WRONG_GUESSES = 6


def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses = 0

    print("=== HANGMAN GAME ===")
    print(f"Guess the word one letter at a time. You have {MAX_WRONG_GUESSES} incorrect guesses.")

    while wrong_guesses < MAX_WRONG_GUESSES:
        display = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )
        print(f"\nWord: {display}")
        print(f"Incorrect guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word!")
            return

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct!")
        else:
            wrong_guesses += 1
            print("Incorrect!")

    print(f"\nGame over! The word was '{secret_word}'.")


if __name__ == "__main__":
    play_hangman()
