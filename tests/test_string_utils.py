import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from src.string_utils import StringUtils


@pytest.fixture
def su():
    """Reusable StringUtils fixture."""
    return StringUtils()


class TestReverse:
    def test_reverse_basic(self, su):
        assert su.reverse("hello") == "olleh"

    def test_reverse_single_char(self, su):
        assert su.reverse("a") == "a"

    def test_reverse_empty_string(self, su):
        assert su.reverse("") == ""

    def test_reverse_palindrome_unchanged(self, su):
        assert su.reverse("madam") == "madam"


class TestPalindrome:
    @pytest.mark.parametrize("word,expected", [
        ("racecar", True),
        ("madam", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("", True),
    ])
    def test_is_palindrome_parametrized(self, su, word, expected):
        """Parametrized edge-case testing for palindrome detection."""
        assert su.is_palindrome(word) == expected


class TestVowelCount:
    def test_count_vowels_basic(self, su):
        assert su.count_vowels("hello") == 2

    def test_count_vowels_uppercase(self, su):
        assert su.count_vowels("AEIOU") == 5

    def test_count_vowels_no_vowels(self, su):
        assert su.count_vowels("gym") == 0

    def test_count_vowels_empty(self, su):
        assert su.count_vowels("") == 0


class TestCapitalizeWords:
    def test_capitalize_basic(self, su):
        assert su.capitalize_words("hello world") == "Hello World"

    def test_capitalize_already_caps(self, su):
        assert su.capitalize_words("Hello World") == "Hello World"

    def test_capitalize_single_word(self, su):
        assert su.capitalize_words("python") == "Python"


class TestPasswordStrength:
    """Edge-case testing for password validation workflow."""

    def test_strong_password(self, su):
        assert su.is_strong_password("Secure@123") is True

    def test_too_short(self, su):
        assert su.is_strong_password("Ab1!") is False

    def test_no_uppercase(self, su):
        assert su.is_strong_password("secure@123") is False

    def test_no_digit(self, su):
        assert su.is_strong_password("Secure@abc") is False

    def test_no_special_char(self, su):
        assert su.is_strong_password("Secure123") is False

    def test_boundary_length(self, su):
        """Edge case: exactly 8 characters meeting all criteria."""
        assert su.is_strong_password("Ab1!wxyz") is True
