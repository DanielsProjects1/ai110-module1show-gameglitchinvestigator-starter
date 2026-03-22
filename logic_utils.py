def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty.

    This function centralizes the difficulty -> range mapping so the app
    and any tests use the same canonical source of truth.

    Mappings:
    - "Easy": (1, 20)
    - "Normal": (1, 50)
    - "Hard": (1, 100)

    If an unknown difficulty string is provided, the function defaults to
    (1, 100) which matches the original app behavior.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        # Swapped: Normal now uses the range that used to be for Hard
        return 1, 50
    if difficulty == "Hard":
        # Swapped: Hard now uses the range that used to be for Normal
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    # Normalize whitespace so inputs like "   " are treated as empty
    raw = raw.strip()

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Normalize types: try to coerce both guess and secret to integers
    try:
        # If guess is float-like in string form, convert via float -> int like the parser does
        if isinstance(guess, str) and "." in guess:
            guess_val = int(float(guess))
        else:
            guess_val = int(guess)
    except Exception:
        # If guess cannot be converted, keep as-is for fallback comparisons
        guess_val = guess

    try:
        if isinstance(secret, str) and "." in secret:
            secret_val = int(float(secret))
        else:
            secret_val = int(secret)
    except Exception:
        secret_val = secret

    # If both values are ints (or coercible to ints), compare numerically
    try:
        if guess_val == secret_val:
            return "Win"
        if guess_val > secret_val:
            return "Too High"
        return "Too Low"
    except Exception:
        # Fallback to string comparison if numeric comparison fails
        g = str(guess_val)
        s = str(secret_val)
        if g == s:
            return "Win"
        if g > s:
            return "Too High"
        return "Too Low"


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        points = 100 - 10 * attempt_number
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
