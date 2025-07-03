#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#

# @lc code=start
from typing import List


class Solution:
    # First solution, brute force
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     missed = []
    #     for i in range(1, len(nums) + 1):
    #         if i not in nums:
    #             missed.append(i)
    #     return missed

    # Alternative set-based solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     return list(set(range(1, n + 1)) - set(nums))

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Mark indices corresponding to numbers seen
        for num in nums:
            idx = abs(num) - 1
            if nums and idx < len(nums) and nums[idx] > 0:
                nums[idx] = -nums[idx]
        # Collect indices with positive values (missing numbers)
        return [i + 1 for i, num in enumerate(nums) if num > 0]


# @lc code=end

import pytest


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
        ([1, 1], [2]),
        ([1, 2, 3, 4, 5], []),
        ([2, 2], [1]),
        ([1], []),
        ([2], [1]),
        ([1, 1, 2, 2], [3, 4]),
        ([3, 3, 3, 3], [1, 2, 4]),
        ([], []),
    ],
)
def test_findDisappearedNumbers(nums, expected):
    assert sorted(Solution().findDisappearedNumbers(nums)) == sorted(expected)
