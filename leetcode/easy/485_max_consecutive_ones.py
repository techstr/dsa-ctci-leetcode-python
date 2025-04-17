#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Finds the maximum number of consecutive 1s in a binary array.
    Args:
        nums (List[int]): A list of integers containing only 0s and 1s.
    Returns:
        int: The maximum count of consecutive 1s in the input list.
    """

    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    #     max_ones = 0
    #     start = 0
    #     end = 0
    #     flip = False
    #     while end < len(nums):
    #         if flip and nums[end] != 1:
    #             max_ones = (end - start) if max_ones < (end - start) else max_ones
    #             flip = False
    #         if not flip and nums[end] == 1:
    #             start = end
    #             flip = True
    #         end += 1

    #     if flip:
    #         max_ones = (end - start) if max_ones < (end - start) else max_ones

    #     return max_ones

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        current_ones = 0

        for num in nums:
            if num == 1:
                current_ones += 1
                max_ones = max(max_ones, current_ones)
            else:
                current_ones = 0

        return max_ones


# @lc code=end
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1, 0, 1, 1, 1], 3),  # Consecutive ones: [1, 1, 1]
        ([1, 0, 1, 1, 0, 1], 2),  # Consecutive ones: [1, 1]
        ([0, 0, 0, 0], 0),  # No ones
        ([1, 1, 1, 1], 4),  # All ones
        ([1, 0, 0, 1, 0, 1, 1], 2),  # Consecutive ones: [1, 1]
        ([0, 1, 0, 1, 0, 1], 1),  # Single ones
        ([], 0),  # Empty list
    ],
)
def test_findMaxConsecutiveOnes(nums, expected):
    solution = Solution()
    assert solution.findMaxConsecutiveOnes(nums) == expected
