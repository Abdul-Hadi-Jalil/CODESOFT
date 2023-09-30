from random import choice
from random import shuffle


class PasswordGenerator:
    UPPERCASE_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LOWERCASE_CHARACTERS = "abcdefghijklmnopqrstuvwxyz"
    NUMBERS = "0123456789"
    SPECIAL_CHARACTERS = "!@#$%^&*()_+=-{}[]|:;,<>.?/~"
    LENGTH_LIMIT = 30

    def __init__(self, length=10, uppercase=True, lowercase=True, numbers=True, special_characters=True):
        self.length = length
        self.include_chars = set()
        self.repeat_characters = {}

        if uppercase:
            self.include_chars.update(self.UPPERCASE_CHARACTERS)
        if lowercase:
            self.include_chars.update(self.LOWERCASE_CHARACTERS)
        if numbers:
            self.include_chars.update(self.NUMBERS)
        if special_characters:
            self.include_chars.update(self.SPECIAL_CHARACTERS)

        self.excluded_characters = set()

    def generate(self) -> str:
        length = self.length
        if not self.include_chars:
            raise ValueError("No character sets selected for password generation")

        if self.length > self.LENGTH_LIMIT:
            raise ValueError("The specified length exceeds the maximum limit (30 characters)")

        if self.length < 0:
            raise ValueError("Password length becomes negative after repeating characters")

        password_chars = self.include_chars - self.excluded_characters

        password = []
        for char, count in self.repeat_characters.items():
            password.extend(char * count)
            self.length -= count
            if self.length < 1: break
        password.extend(choice(list(password_chars)) for _ in range(length))
        shuffle(password)
        return ''.join(password)

    def exclude_characters(self, characters):
        self.excluded_characters.update(characters)

    def include_characters(self, characters):
        self.include_chars.update(characters)

    def repeated_characters(self, characters_to_repeat):
        self.repeat_characters = characters_to_repeat
