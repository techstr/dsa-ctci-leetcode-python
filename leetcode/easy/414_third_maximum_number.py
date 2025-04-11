#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Given an integer array `nums`, this method returns the third distinct maximum number in the array.
    If the third maximum does not exist, it returns the maximum number.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        int: The third distinct maximum number if it exists; otherwise, the maximum number.
    """

    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float("-inf")
        for num in nums:
            if num in (first, second, third):
                continue
            if num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num
        return third if third != float("-inf") else first


# @lc code=end
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 2, 1], 1),  # Third distinct maximum exists
        ([1, 2], 2),  # Third distinct maximum does not exist, return max
        ([2, 2, 3, 1], 1),  # Third distinct maximum exists with duplicates
        ([1, 1, 1], 1),  # All elements are the same, return max
        ([5, 2, 2, 4, 1], 2),  # Third distinct maximum exists
        ([1], 1),  # Single element, return max
        ([1, 2, 2, 3], 1),  # Third distinct maximum exists with duplicates
        ([10, 9, 8, 7], 8),  # Third distinct maximum exists
    ],
)
def test_third_max(nums, expected):
    solution = Solution()
    assert solution.thirdMax(nums) == expected
