def hangman(word: str = "java", no_of_tries: int = 6):
    # Check if the word is alphabetical
    if not word.isalpha():
        raise ValueError("Word should only contain alphabetical characters")

    # Check if the word has whitespace
    if " " in word:
        raise ValueError("Word should not have whitespaces")

    # Check if no_of_tries is greater than zero
    if no_of_tries <= 0:
        raise ValueError("The number of tries should be greater than zero")

    # Set the number of underscores to equal the number of letters in the word
    used_letters = []
    correct_guesses = ["_" for _ in range(len(word))]

    while no_of_tries > 0:
        print(f"\nYou have {no_of_tries} tries left.")
        print(f"Used Letters: {', '.join(used_letters)}")
        print(f"Word: {' '.join(correct_guesses)}")

        guess = input("Guess a letter: ")
        if not guess.isalpha():
            print("Kindly input a letter.\n")
            continue

        guess = guess.lower()
        if guess in used_letters:
            print("You've already guessed that letter. Try again.\n")
            continue

        used_letters.append(guess)

        if guess in word.lower():
            for i, letter in enumerate(word.lower()):
                if letter == guess:
                    correct_guesses[i] = word[i]
        else:
            print("That letter is not in the word. Try again.\n")

        if "_" not in correct_guesses:
            print(f"You guessed the word {word}! 🥳\n")
            return

        no_of_tries -= 1

    print(f"The correct word was: {word}")
    print("Game Over! 😔\n")


if __name__ == "__main__":
    hangman()
    # hangman("potato")
    # hangman("Nelson Ombuya", 10)
