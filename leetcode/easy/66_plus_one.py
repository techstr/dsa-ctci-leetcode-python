#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    A class used to solve the 'Plus One' problem.

    Methods
    -------
    plusOne(digits: List[int]) -> List[int]
    Takes a list of integers representing a non-negative integer and
    returns a new list of integers representing the integer plus one.
    Increment the integer represented by the list of digits by one.

    Parameters
    ----------
    digits : List[int]
        A list of integers where each element represents a single digit
        of a non-negative integer. The most significant digit is at the
        start of the list.

    Returns
    -------
    List[int]
        A list of integers representing the input integer incremented by one.
        If there is a carry-over that results in an additional digit, the
        list will be extended accordingly.

    Example
    -------
    Input: [1, 2, 3]
    Output: [1, 2, 4]

    Input: [9, 9, 9]
    Output: [1, 0, 0, 0]
    """

    def plusOne(self, digits: List[int]) -> List[int]:
        # Start from the last digit and iterate backwards
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                # If the current digit is less than 9, increment it and return
                digits[i] += 1
                return digits
            # If the digit is 9, set it to 0 and continue to the next digit
            digits[i] = 0
        # If all digits were 9, we need to add a leading 1
        return [1] + digits


# @lc code=end


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([1, 2, 3], [1, 2, 4]),  # Simple case
        ([4, 3, 2, 1], [4, 3, 2, 2]),  # Another simple case
        ([0], [1]),  # Single digit zero
        ([9], [1, 0]),  # Single digit nine
        ([9, 9], [1, 0, 0]),  # Multiple nines
        ([1, 9, 9], [2, 0, 0]),  # Mixed digits with carry
    ],
)
def test_plus_one(digits, expected):
    solution = Solution()
    assert solution.plusOne(digits) == expected
