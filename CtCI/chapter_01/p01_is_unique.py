import pytest


def is_unique_chars_algorithmic(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    # this is a pythonic and faster way to initialize an array with a fixed value.
    #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


def is_unique_chars_pythonic(string):
    return len(set(string)) == len(string)


def is_unique_bit_vector(string):
    """Uses bitwise operation instead of extra data structures."""
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    checker = 0
    for c in string:
        val = ord(c)
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True


def is_unique_chars_using_dictionary(string: str) -> bool:
    character_counts = {}
    for char in string:
        if char in character_counts:
            return False
        character_counts[char] = 1
    return True


def is_unique_chars_using_set(string: str) -> bool:
    characters_seen = set()
    for char in string:
        if char in characters_seen:
            return False
        characters_seen.add(char)
    return True


# O(NlogN)
def is_unique_chars_sorting(string: str) -> bool:
    sorted_string = sorted(string)
    last_character = None
    for char in sorted_string:
        if char == last_character:
            return False
        last_character = char
    return True


# Sorting without extra variable. TC: O(NlogN) SC: O(1) Con: Modifies input string
def is_unique_chars_sort(string: str) -> bool:
    string = sorted(string)
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            return False
    return True


test_cases = [
    ("abcd", True),
    ("s4fad", True),
    ("", True),
    ("23ds2", False),
    ("hb 627jh=j ()", False),
    ("".join([chr(val) for val in range(128)]), True),  # unique 128 chars
    ("".join([chr(val // 2) for val in range(129)]), False),  # non-unique 129 chars
]

test_functions = [
    is_unique_chars_pythonic,
    is_unique_chars_algorithmic,
    is_unique_bit_vector,
    is_unique_chars_using_dictionary,
    is_unique_chars_using_set,
    is_unique_chars_sorting,
    is_unique_chars_sort,
]


@pytest.mark.parametrize("func", test_functions)
@pytest.mark.parametrize("text,expected", test_cases)
def test_is_unique_chars(func, text, expected):
    assert func(text) == expected, f"{func.__name__} failed for value: {text}"
