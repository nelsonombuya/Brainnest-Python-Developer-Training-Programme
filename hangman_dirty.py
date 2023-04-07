"""
    The hangman game is a word guessing game where the player is given a word
    and has to guess the letters that make up the word.

    The player is given a certain number of tries (no more than 6 wrong guesses
    are allowed) to guess the correct letters before the game is over.
"""

# Output
"""
You have 6 tries left.
Used letters:
Word: _ _ _ _
Guess a letter: a

You have 6 tries left.
Used letters: a
Word: _ a _ a
Guess a letter: j

You have 6 tries left.
Used letters: j a
Word: j a _ a
Guess a letter: v
You guessed the word java !
"""
# * Initial Implementation
word = "java"
no_of_tries = 6
used_letters = []
correct_guesses = []
[correct_guesses.append("_") for letter in word]

while no_of_tries > 0:
    """
    Process:
    -TODO Number of tries
    -TODO Used Letters
    -TODO Word
    -TODO Guess a letter
    """

    try:
        print(f"You have {no_of_tries} tries left.")

        """
        Used letters depend on the letters that the user has guessed
        So the list will be obtained from user input

        -TODO Get User input
        -TODO Save input in array
        -TODO Print user input in the described way
        -TODO Try catch when user inputs a number
        """
        print(f"Used Letters: {', '.join(used_letters)}")

        """
            Word
            We need to print an underscore for each letter in the word
        """
        print(f"Word: {' '.join(correct_guesses)}")

        guess = input("Guess a letter: ")
        if guess.isalpha():
            used_letters.append(guess)
        else:
            raise TypeError("Kindly input a letter.")

        """
            Now to determine the win condition
            -TODO We'll need to check for the letter in the word, and how
            many times it appears.
            -TODO Next, we'll need to update the correctly guessed letters
            -TODO We check if there's still '_' in the correct guesses
            -TODO If there is, continue
            -TODO If there isn't, give the win
        """
        for index, letter in enumerate(word):
            if guess == letter:
                correct_guesses[index] = letter

        if "_" not in correct_guesses:
            print(f"You guessed the word {word}!")
            break

        no_of_tries -= 1
        print()  # Prints an empty new line
    except TypeError as error:
        print(error)
    except Exception as exception:
        print(f"Something went wrong. Exception Message: {exception}")


"""
    Now, for code clean up and refactoring
"""


def hangman(word: str = "java", no_of_tries: int = 6):
    used_letters = []

    # Set the number of underscores to equal the number of letters in the word
    correct_guesses = []
    [correct_guesses.append("_") for letter in word]

    while no_of_tries > 0:
        try:
            print(f"You have {no_of_tries} tries left.")
            print(f"Used Letters: {', '.join(used_letters)}")
            print(f"Word: {' '.join(correct_guesses)}")
            guess = input("Guess a letter: ")

            # Checking if guess is a letter
            if guess.isalpha():
                used_letters.append(guess)
            else:
                raise TypeError("Kindly input a letter.")

            # Checking for the guessed letter in the word
            # And updating the correctly guessed letters
            for index, letter in enumerate(word):
                if guess == letter:
                    correct_guesses[index] = letter

            # Checking if all of the letters have been guessed correctly
            if "_" not in correct_guesses:
                print(f"You guessed the word {word}!")
                break

            no_of_tries -= 1
            print()  # Prints an empty new line
        except TypeError as error:
            print(error)
        except Exception as exception:
            print(f"Something went wrong. Exception Message: {exception}")
