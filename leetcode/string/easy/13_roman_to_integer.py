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
    "name,s,expected",
    [
        ("basic_case           ", "III", 3),
        ("subtraction_case_IV  ", "IV", 4),
        ("subtraction_case_IX  ", "IX", 9),
        ("multiple_symbols     ", "LVIII", 58),
        ("complex_case         ", "MCMXCIV", 1994),
        ("smallest_roman       ", "I", 1),
        ("largest_roman        ", "MMMCMXCIX", 3999),
        ("subtraction_L        ", "XL", 40),
        ("subtraction_C        ", "XC", 90),
        ("subtraction_D        ", "CD", 400),
        ("subtraction_M        ", "CM", 900),
        ("mixed_case           ", "MMXXV", 2025),
        ("repeated_symbols     ", "DCCC", 800),
        ("random_case_1        ", "CCCLXV", 365),
        ("random_case_2        ", "MDCLXVI", 1666),
        ("random_case_3        ", "MCMXLV", 1945),
        ("random_case_4        ", "MMXIX", 2019),
    ],
)
def testRomanToInt(name, s, expected):
    solution = Solution()
    assert solution.romanToInt(s) == expected, name
