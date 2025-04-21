#
# @lc app=leetcode id=961 lang=python3
#
# [961] N-Repeated Element in Size 2N Array
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Class Solution contains a method to find the element repeated N times in an array of size 2N.

    Methods:
        repeatedNTimes(nums: List[int]) -> int:
            Given an integer array nums of size 2N, where there are N+1 unique elements
            and one element is repeated N times, this method returns the element that is repeated N times.

    Args:
        nums (List[int]): The input array of integers of size 2N.

    Returns:
        int: The element that is repeated N times in the array.
    """

    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1  # This line should never be reached for valid inputs


# @lc code=end


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 3], 3),  # Simple case where 3 is repeated
        ([2, 1, 2, 5, 3, 2], 2),  # Case where 2 is repeated
        ([5, 1, 5, 2, 5, 3, 5, 4], 5),  # Case where 5 is repeated multiple times
        ([9, 9, 9, 9], 9),  # All elements are the same
        ([1, 1, 2, 3, 4, 1], 1),  # Case where 1 is repeated
        ([6, 6, 6, 6, 6, 6], 6),  # All elements are the same
        ([1, 2, 3, 4, 5, 6, 7, 1], 1),  # Repeated element at the end
    ],
)
def test_repeatedNTimes(nums, expected):
    solution = Solution()
    assert solution.repeatedNTimes(nums) == expected
