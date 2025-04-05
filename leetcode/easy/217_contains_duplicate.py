#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Class Solution provides a method to determine if a list of integers contains any duplicates.

    Methods:
        containsDuplicate(nums: List[int]) -> bool:
            Checks if the input list contains any duplicate elements.
            Args:
                nums (List[int]): A list of integers to check for duplicates.
            Returns:
                bool: True if duplicates are found, False otherwise.
    """

    # def containsDuplicate(self, nums: List[int]) -> bool:
    #     return len(nums) != len(set(nums))

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if the input list contains any duplicate elements.
        This method uses a set to track seen elements and returns True if any duplicates are found.
        Time complexity is O(n) and space complexity is O(n).
        But the solution exists as soon as a duplicate is found

        Args:
            nums (List[int]): A list of integers to check for duplicates.

        Returns:
            bool: True if duplicates are found, False otherwise.
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


# @lc code=end


@pytest.mark.array
@pytest.mark.hash_table
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),  # Duplicate exists
        ([1, 2, 3, 4], False),  # No duplicates
        ([1, 1, 1, 1], True),  # All elements are duplicates
        ([], False),  # Empty list
        ([1], False),  # Single element, no duplicates
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1], True),  # Duplicate at the end
    ],
)
def test_contains_duplicate(nums, expected):
    solution = Solution()
    assert solution.containsDuplicate(nums) == expected
