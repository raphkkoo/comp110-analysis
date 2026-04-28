"""Structured Wordle"""

__author__: str = "730748337"


def input_guess(expected_len: int) -> str:
    guess: str = input(f"Enter a {expected_len} character word: ")

    # repeat question over and over til they get it right
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")

    return guess


def contains_char(word: str, single_char: str) -> bool:
    assert len(single_char) == 1
    index: int = 0
    while index < len(word):
        if word[index] == single_char:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)

    WHITE_BOX: str = "\U00002b1c"
    GREEN_BOX: str = "\U0001f7e9"
    YELLOW_BOX: str = "\U0001f7e8"

    result_emojis: str = ""
    index: int = 0

    # Loop through each character of the guess to determine the box color
    while index < len(guess):
        if guess[index] == secret[index]:
            # Exact match at the same position
            result_emojis += GREEN_BOX
        else:
            if contains_char(secret, guess[index]):
                result_emojis += YELLOW_BOX
            else:
                result_emojis += WHITE_BOX
        index += 1

    return result_emojis


def main(secret: str) -> None:
    turns_taken: int = 1
    max_turns: int = 6
    user_won: bool = False

    # The game continues if there are still turns
    while turns_taken <= max_turns and not user_won:
        print(f"=== Turn {turns_taken}/6 ===")

        current_guess: str = input_guess(len(secret))

        print(emojified(current_guess, secret))

        # Check if the guess is perfectly correct
        if current_guess == secret:
            user_won = True
        else:
            turns_taken += 1

    # Final game state reporting
    if user_won:
        print(f"You won in {turns_taken}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
