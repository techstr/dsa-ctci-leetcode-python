#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#


# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Removes duplicates from a sorted array in-place such that each element appears only once.

    Args:
        nums (List[int]): A list of integers sorted in non-decreasing order.

    Returns:
        int: The length of the modified array with unique elements.

    Note:
        The input list `nums` is modified in-place to contain only the unique elements
        in the first part of the list. The relative order of the elements is maintained.
        The elements beyond the returned length are not guaranteed to be in any specific order.
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write_index = 1  # Index to write the next unique element
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1

        return write_index


# @lc code=end


@pytest.mark.parametrize(
    "nums, expected_length, expected_nums",
    [
        ([1, 1, 2], 2, [1, 2]),  # Basic case with duplicates
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),  # Multiple duplicates
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),  # No duplicates
        ([1, 1, 1, 1, 1], 1, [1]),  # All elements are the same
        ([], 0, []),  # Empty list
        ([1], 1, [1]),  # Single element
    ],
)
def test_remove_duplicates(nums, expected_length, expected_nums):
    solution = Solution()
    length = solution.removeDuplicates(nums)
    assert length == expected_length
    assert nums[:length] == expected_nums  # Adding a delay of 1 second
