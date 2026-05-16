class StringUtils:
    """String utility functions for validation and transformation."""

    def reverse(self, s):
        return s[::-1]

    def is_palindrome(self, s):
        cleaned = s.replace(" ", "").lower()
        return cleaned == cleaned[::-1]

    def count_vowels(self, s):
        return sum(1 for c in s.lower() if c in "aeiou")

    def capitalize_words(self, s):
        return " ".join(word.capitalize() for word in s.split())

    def is_strong_password(self, password):
        """
        Returns True if password:
        - is at least 8 characters
        - has at least one uppercase letter
        - has at least one digit
        - has at least one special character
        """
        if len(password) < 8:
            return False
        if not any(c.isupper() for c in password):
            return False
        if not any(c.isdigit() for c in password):
            return False
        if not any(c in "!@#$%^&*()_+-=[]{}|;:',.<>?/" for c in password):
            return False
        return True
