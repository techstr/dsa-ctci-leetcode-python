#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#


# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Moves all zeroes in the given list to the end while maintaining the relative order
    of the non-zero elements. The operation is performed in-place without creating a
    new list.

    Args:
        nums (List[int]): The list of integers to be modified.

    Returns:
        None: The function modifies the input list in-place and does not return anything.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return nums
        start = 0
        index = 1
        while index < len(nums):
            if nums[start] == 0:
                nums[start] = nums[index]
                nums[index] = 0
            if nums[start] != 0:
                start += 1
            index += 1


# @lc code=end


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0, 0, 1], [1, 0, 0]),
        ([1, 0, 0, 2, 3], [1, 2, 3, 0, 0]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 2, 3], [1, 2, 3]),
        ([0], [0]),
        ([1], [1]),
    ],
)
def test_move_zeroes(nums, expected):
    solution = Solution()
    nums_copy = nums.copy()
    solution.moveZeroes(nums_copy)
    assert nums_copy == expected
