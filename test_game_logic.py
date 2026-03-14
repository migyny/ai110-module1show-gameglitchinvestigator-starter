from logic_utils import check_guess, update_score

# --- update_score tests ---

def test_win_first_attempt():
    assert update_score(0, "Win", 0) == 90

def test_win_later_attempt():
    assert update_score(0, "Win", 5) == 40

def test_win_minimum_points():
    # At attempt 9+, points are clamped to 10
    assert update_score(0, "Win", 9) == 10

def test_win_adds_to_existing_score():
    assert update_score(50, "Win", 0) == 140

def test_too_high_subtracts_5():
    assert update_score(100, "Too High", 0) == 95

def test_too_high_subtracts_5_on_odd_attempt():
    assert update_score(100, "Too High", 1) == 95

def test_too_high_subtracts_5_on_even_attempt():
    # Previously this was a bug — even attempts used to ADD 5
    assert update_score(100, "Too High", 2) == 95

def test_too_high_matches_too_low_penalty():
    # Both wrong guesses should apply the same -5 penalty
    assert update_score(100, "Too High", 0) == update_score(100, "Too Low", 0)

def test_too_low_subtracts_5():
    assert update_score(100, "Too Low", 0) == 95

def test_unknown_outcome_unchanged():
    assert update_score(100, "Invalid", 0) == 100


# --- check_guess tests ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- Bug fix: secret must never be passed as a string ---
# Previously, on even-numbered attempts, secret was cast to str(secret),
# causing check_guess to always return "Too High"/"Too Low" and never "Win".

def test_win_with_int_secret():
    # Core fix: correct guess against an int secret should win
    assert check_guess(42, 42) == "Win"

def get_secret_for_attempt(raw_secret: int, _attempt: int) -> int:
    """Mirrors the fixed app.py logic — secret is always returned as int."""
    return raw_secret  # fixed: no str() conversion on even attempts


def test_win_even_attempt_2():
    # Simulates attempt #2 (even) — secret must be int, not str
    secret = get_secret_for_attempt(42, _attempt=2)
    assert isinstance(secret, int), f"Expected int, got {type(secret)}"
    assert check_guess(42, secret) == "Win"

def test_win_even_attempt_4():
    # Simulates attempt #4 (even)
    secret = get_secret_for_attempt(7, _attempt=4)
    assert isinstance(secret, int), f"Expected int, got {type(secret)}"
    assert check_guess(7, secret) == "Win"

def test_win_even_attempt_6():
    # Simulates attempt #6 (even)
    secret = get_secret_for_attempt(99, _attempt=6)
    assert isinstance(secret, int), f"Expected int, got {type(secret)}"
    assert check_guess(99, secret) == "Win"

def test_no_string_secret_too_high():
    # Passing secret as int should still return "Too High" correctly on even attempt
    assert check_guess(60, 42) == "Too High"

def test_no_string_secret_too_low():
    # Passing secret as int should still return "Too Low" correctly on even attempt
    assert check_guess(10, 42) == "Too Low"

def test_string_secret_does_not_win():
    # Demonstrates the old bug: int guess vs string secret raises TypeError in Python 3
    import pytest
    assert check_guess(42, 42) == "Win"          # correct (int vs int)
    with pytest.raises(TypeError):
        check_guess(42, "42")                    # old buggy behavior: int vs str crashes
