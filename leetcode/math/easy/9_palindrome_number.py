#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#


# @lc code=start
import pytest


class Solution:
    """
    A class used to determine if a given integer is a palindrome.

    Methods
    -------
    isPalindrome(x: int) -> bool
        Determines whether the given integer `x` is a palindrome.
    """

    # def isPalindrome(self, x: int) -> bool:
    #     for i in range(len(str(x)) // 2):
    #         if str(x)[i] != str(x)[-i - 1]:
    #             return False
    #     return True

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10


# @lc code=end


@pytest.mark.parametrize(
    "test,expected",
    [
        (121, True),  # Palindrome number
        (-121, False),  # Negative number, not a palindrome
        (10, False),  # Number with different first and last digits
        (12321, True),  # Odd-length palindrome number
        (123321, True),  # Even-length palindrome number
        (0, True),  # Zero is a palindrome
        (1001, True),  # Palindrome with zeros in the middle
        (100, False),  # Number ending with zero, not a palindrome
    ],
)
def testIsPalindrome(test, expected):
    solution = Solution()
    # Test cases for positive scenarios
    assert solution.isPalindrome(test) is expected
