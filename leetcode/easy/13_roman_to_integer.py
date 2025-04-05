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


@pytest.mark.math
@pytest.mark.string
@pytest.mark.parametrize(
    "s,expected",
    [
        # Basic cases
        ("III", 3),  # Simple addition
        ("IV", 4),  # Subtraction case - I before V
        ("IX", 9),  # Subtraction case - I before X
        # Medium complexity cases
        ("LVIII", 58),  # L=50, V=5, III=3
        ("MCMXCIV", 1994),  # M=1000, CM=900, XC=90, IV=4
        # Edge cases
        ("I", 1),  # Smallest roman numeral
        ("MMMCMXCIX", 3999),  # Largest roman numeral in common usage
        # Subtraction cases
        ("XL", 40),  # X before L
        ("XC", 90),  # X before C
        ("CD", 400),  # C before D
        ("CM", 900),  # C before M
        # Various combinations
        ("MMXXV", 2025),  # Simple addition case
        ("DCCC", 800),  # Repeated symbols
        ("CCCLXV", 365),  # Year representation
        ("MDCLXVI", 1666),  # Ascending symbols
        ("MCMXLV", 1945),  # World War II end year
        ("MMXIX", 2019),  # Recent year
    ],
)
def testRomanToInt(s, expected):
    solution = Solution()
    assert solution.romanToInt(s) == expected
