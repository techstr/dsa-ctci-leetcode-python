#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#


# @lc code=start
from typing import List

import pytest


class Solution:
    """
    A class containing a method to find the index at which a target value should be inserted
    into a sorted list of integers.

    Methods:
        searchInsert(nums: List[int], target: int) -> int:
            Determines the index at which the target value should be inserted in the sorted list.
    """

    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left + 1 if nums[left] < target else left


# @lc code=end


@pytest.mark.array
@pytest.mark.binary_search
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([1, 3, 5, 6], 5, 2),  # Target exists in the list
        ([1, 3, 5, 6], 2, 1),  # Target should be inserted at index 1
        ([1, 3, 5, 6], 7, 4),  # Target should be inserted at the end
        ([1, 3, 5, 6], 0, 0),  # Target should be inserted at the beginning
        ([1], 0, 0),  # Single element list, target less than the element
        ([1], 2, 1),  # Single element list, target greater than the element
        ([], 3, 0),  # Empty list, target should be inserted at index 0
    ],
)
def test_search_insert(nums, target, expected):
    solution = Solution()
    assert solution.searchInsert(nums, target) == expected
