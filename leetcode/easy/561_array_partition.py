#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Given an integer array `nums` of 2n integers, this method groups these integers
    into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi)
    for all i is maximized. It returns the maximum sum.

    Args:
        nums (List[int]): A list of 2n integers.

    Returns:
        int: The maximum sum of min(ai, bi) for all i after pairing.
    """

    # def arrayPairSum(self, nums: List[int]) -> int:
    #     nums = sorted(nums)
    #     max_sum = 0
    #     for i in range(0, len(nums), 2):
    #         max_sum += min(nums[i], nums[i + 1])
    #     return max_sum

    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the array and sum every second element (even indices)
        return sum(sorted(nums)[::2])


# @lc code=end


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 4, 3, 2], 4),  # Example case: pairs (1, 2) and (3, 4) -> min(1, 2) + min(3, 4) = 4
        ([6, 2, 6, 5, 1, 2], 9),  # Pairs (1, 2), (2, 5), (6, 6) -> min(1, 2) + min(2, 5) + min(6, 6) = 9
        ([1, 2], 1),  # Single pair (1, 2) -> min(1, 2) = 1
        ([7, 3, 1, 0, 0, 6], 7),  # Pairs (0, 0), (1, 3), (6, 7) -> min(0, 0) + min(1, 3) + min(6, 7) = 7
        ([1, 1, 1, 1], 2),  # Pairs (1, 1), (1, 1) -> min(1, 1) + min(1, 1) = 2
    ],
)
def test_arrayPairSum(nums, expected):
    solution = Solution()
    assert solution.arrayPairSum(nums) == expected
