#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
import pytest


class Solution:
    """
    Reverse the vowels in a given string.

    This method takes a string `s` as input and returns a new string where
    the vowels in `s` are reversed, while the positions of all other characters
    remain unchanged.

    Vowels are defined as 'a', 'e', 'i', 'o', 'u' (both uppercase and lowercase).

    Args:
        s (str): The input string.

    Returns:
        str: A new string with the vowels reversed.
    """

    def reverseVowels(self, s: str) -> str:
        VOWELS = set("AEIOUaeiou")
        chars = list(s)
        start, end = 0, len(chars) - 1
        while start < end:
            while start < end and chars[start] not in VOWELS:
                start += 1
            while start < end and chars[end] not in VOWELS:
                end -= 1
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
        return "".join(chars)


# @lc code=end


@pytest.mark.parametrize(
    "input_string, expected_output",
    [
        ("hello", "holle"),  # Basic test with lowercase vowels
        ("leetcode", "leotcede"),  # Multiple vowels in a string
        ("aA", "Aa"),  # Case sensitivity test
        ("", ""),  # Empty string test
        ("bcdfg", "bcdfg"),  # No vowels in the string
        ("aeiou", "uoiea"),  # All vowels in order
        ("AEIOU", "UOIEA"),  # All uppercase vowels
        ("hEllo wOrld", "hOllo wErld"),  # Mixed case and spaces
        ("a", "a"),  # Single vowel
        ("b", "b"),  # Single consonant
    ],
)
def test_reverse_vowels(input_string, expected_output):
    solution = Solution()
    assert solution.reverseVowels(input_string) == expected_output
