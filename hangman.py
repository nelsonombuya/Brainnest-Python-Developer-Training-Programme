def hangman(word: str = "java", no_of_tries: int = 6):
    try:
        # Checking if the word has a whitespace
        if " " in word:
            raise Exception("Word should not have whitespaces")

        # Checking if no_of_tries is greater than zero
        if no_of_tries <= 0:
            raise Exception("The number of tries should be greater than zero")
    except Exception as exception:
        print(f"{exception} - Word: '{word}', Number of Tries: {no_of_tries}")
        return

    # Set the number of underscores to equal the number of letters in the word
    used_letters = []
    correct_guesses = []
    [correct_guesses.append("_") for letter in word]

    while True:
        try:
            print(f"\nYou have {no_of_tries} tries left.")
            print(f"Used Letters: {', '.join(used_letters)}")
            print(f"Word: {' '.join(correct_guesses)}")
            guess = input("Guess a letter: ")

            # Checking if guess is a letter
            if guess.isalpha():
                used_letters.append(guess)
            else:
                raise TypeError("Kindly input a letter.\n")

            # Checking for the guessed letter in the word
            # And updating the correctly guessed letters
            for index, letter in enumerate(word):
                if guess.lower() == letter.lower():
                    correct_guesses[index] = letter

            # Checking if all of the letters have been guessed correctly
            if "_" not in correct_guesses:
                print(f"You guessed the word {word}! 🥳\n")
                break

            # If the number of tries are over, the player loses
            no_of_tries -= 1
            if no_of_tries <= 0:
                print("Game Over! 😔\n")
                break
        except TypeError as error:
            print(error)
        except Exception as error:
            print(f"Something went wrong. Error Message: {error}")


if __name__ == "__main__":
    hangman()
    # hangman("potato")
    # hangman("Nelson Ombuya", 10)
