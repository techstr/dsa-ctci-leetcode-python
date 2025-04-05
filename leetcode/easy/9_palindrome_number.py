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
    "name,test,expected",
    [
        ("Palindrome Number                             ", 121, True),
        ("Negative number, not a palindrome             ", -121, False),
        ("Number with different first and last digits   ", 10, False),
        ("Odd-length palindrome number                  ", 12321, True),
        ("Even-length palindrome number                 ", 123321, True),
        ("Zero is a palindrome                          ", 0, True),
        ("Palindrome with zeros in the middle           ", 1001, True),
        ("Number ending with zero, not a palindrome     ", 100, False),
    ],
)
def testIsPalindrome(name, test, expected):
    solution = Solution()
    assert solution.isPalindrome(test) is expected, name
