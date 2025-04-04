#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Class Solution provides a method to solve the Two Sum problem.

    Methods:
        twoSum(nums: List[int], target: int) -> List[int]:
            Given an array of integers `nums` and an integer `target`, this method
            returns the indices of the two numbers such that they add up to `target`.

            Parameters:
                nums (List[int]): A list of integers.
                target (int): The target sum.

            Returns:
                List[int]: A list containing the indices of the two numbers that add up to `target`.

            Complexity:
                Time: O(n), where n is the length of `nums`.
                Space: O(n), where n is the length of `nums`.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memoized = {}
        for i, num in enumerate(nums):
            if target - num in memoized:
                return [memoized[target - num], i]
            memoized[num] = i
        return []


# @lc code=end


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),  # Basic test case
        ([3, 2, 4], 6, [1, 2]),  # Test case with non-adjacent indices
        ([3, 3], 6, [0, 1]),  # Test case with duplicate numbers
        ([1, 2, 3, 4, 5], 8, [2, 4]),  # Test case with larger array
        ([5, 75, 25], 100, [1, 2]),  # Test case with larger numbers
        ([1, 2, 3], 7, []),  # Test case with no solution
    ],
)
def test_two_sum(nums, target, expected):
    solution = Solution()
    assert solution.twoSum(nums, target) == expected
