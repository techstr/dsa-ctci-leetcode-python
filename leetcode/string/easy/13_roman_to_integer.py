#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#


# @lc code=start
import pytest


class Solution:
    """
    A class to convert Roman numerals to integers.

    Methods
    -------
    romanToInt(s: str) -> int
        Converts a Roman numeral string to its integer representation.
    """

    def romanToInt(self, s: str) -> int:
        roman_val = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        total = 0
        n = len(s)

        for i in range(n):
            if i < n - 1 and roman_val[s[i]] < roman_val[s[i + 1]]:
                total -= roman_val[s[i]]
            else:
                total += roman_val[s[i]]
        return total


# @lc code=end
@pytest.mark.parametrize(
    "s, expected",
    [
        ("III", 3),  # Basic case
        ("IV", 4),  # Case with subtraction
        ("IX", 9),  # Case with subtraction
        ("LVIII", 58),  # Case with multiple symbols
        ("MCMXCIV", 1994),  # Case with subtraction and multiple symbols
        ("I", 1),  # Smallest Roman numeral
        ("MMMCMXCIX", 3999),  # Largest valid Roman numeral
        ("XL", 40),  # Subtraction case with L
        ("XC", 90),  # Subtraction case with C
        ("CD", 400),  # Subtraction case with D
        ("CM", 900),  # Subtraction case with M
        ("MMXXV", 2025),  # Mixed case
        ("DCCC", 800),  # Repeated symbols
        ("CCCLXV", 365),  # Random valid Roman numeral
        ("MDCLXVI", 1666),  # Random valid Roman numeral
        ("MCMXLV", 1945),  # Random valid Roman numeral
        ("MMXIX", 2019),  # Random valid Roman numeral
    ],
)
def testRomanToInt(s, expected):
    solution = Solution()
    assert solution.romanToInt(s) == expected
