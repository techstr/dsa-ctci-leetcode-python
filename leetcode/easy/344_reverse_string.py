#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#


from typing import List

import pytest

# @lc code=start


class Solution:
    """
    Reverses the input list of characters in-place.

    Args:
        s (List[str]): A list of characters to be reversed.

    Returns:
        None: The input list is modified in-place, and no value is returned.
    """

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# @lc code=end


@pytest.mark.parametrize(
    "input_list, expected",
    [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),  # Reverse a normal string
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),  # Reverse a palindrome
        ([], []),  # Empty list
        (["a"], ["a"]),  # Single character
    ],
)
def test_reverseString(input_list: List[str], expected: List[str]):
    solution = Solution()
    input_list_copy = input_list.copy()
    solution.reverseString(input_list_copy)
    assert input_list_copy == expected
