#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Class to solve the problem of finding the missing number in an array.

    Methods:
        missingNumber(nums: List[int]) -> int:
            Finds the missing number in an array containing n distinct numbers
            taken from the range 0 to n.
    """

    # Time Complexity : O(nlogn) due to sorting
    # Space Complexity : O(n) creating a new list after sorting
    # def missingNumber(self, nums: List[int]) -> int:
    #     nums = sorted(nums)
    #     n = len(nums)
    #     i = 0  # The sorted() function does not modify nums in place; it returns a new sorted list.
    #     while i < n:
    #         if i != nums[i]:
    #             return i
    #         i += 1
    #     return i

    # Time Complexity : O(n) Even though there is two pass
    # Space Complexity : O(n) creating a new map/dictionary
    # def missingNumber(self, nums: List[int]) -> int:
    #     memoize = {}
    #     for num in nums:
    #         memoize[num] = True
    #     n = len(nums)
    #     i = 0
    #     while i < n:
    #         if i not in memoize:
    #             return i
    #         i += 1
    #     return i

    # Time Complexity : O(n)
    # Space Complexity : O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2  # Sum of first n natural numbers
        actual_sum = sum(nums)  # Sum of elements in the array
        return expected_sum - actual_sum


# @lc code=end


@pytest.mark.array
@pytest.mark.hash_table
@pytest.mark.math
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 0, 1], 2),  # Missing number is 2
        ([0, 1], 2),  # Missing number is 2
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),  # Missing number is 8
        ([0], 1),  # Missing number is 1
        ([1], 0),  # Missing number is 0
        ([0, 2], 1),  # Missing number is 1
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 10], 9),  # Missing number is 9
    ],
)
def test_missing_number(nums, expected):
    solution = Solution()
    assert solution.missingNumber(nums) == expected
