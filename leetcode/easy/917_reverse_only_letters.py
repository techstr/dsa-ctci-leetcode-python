#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#


# @lc code=start
import pytest


class Solution:
    """
    Reverses only the letters in the given string `s`, keeping all other characters
    in their original positions.

    Args:
        s (str): The input string containing letters and possibly other characters.

    Returns:
        str: A new string where only the letters are reversed, while non-letter
        characters remain in their original positions.

    Example:
        Input: "a-bC-dEf-ghIj"
        Output: "j-Ih-gfE-dCba"
    """

    def reverseOnlyLetters(self, s: str) -> str:
        chars = list(s)
        first, last = 0, len(chars) - 1
        while first < last:
            if not chars[first].isalpha():
                first += 1
                continue
            if not chars[last].isalpha():
                last -= 1
                continue
            chars[first], chars[last] = chars[last], chars[first]
            first += 1
            last -= 1
        return "".join(chars)


# @lc code=end


@pytest.mark.parametrize(
    "input_str, expected_output",
    [
        ("a-bC-dEf-ghIj", "j-Ih-gfE-dCba"),  # Mixed letters and special characters
        ("Test1ng-Leet=code-Q!", "Qedo1ct-eeLg=ntse-T!"),  # Letters, numbers, and special characters
        ("abc", "cba"),  # Only letters
        ("a-bC-dEf-ghIj-", "j-Ih-gfE-dCba-"),  # Ends with a special character
        ("-", "-"),  # Only special character
        ("", ""),  # Empty string
        ("12345", "12345"),  # Only numbers
        ("a", "a"),  # Single letter
        ("a-b", "b-a"),  # Single letter with special character
        ("ABC", "CBA"),  # Only uppercase letters
        ("abcDEF", "FEDcba"),  # Mixed case letters
    ],
)
def test_reverse_only_letters(input_str, expected_output):
    solution = Solution()
    assert solution.reverseOnlyLetters(input_str) == expected_output
