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
        return 0


# @lc code=end


@pytest.mark.parametrize(
    "name, nums, expected_length, expected_nums",
    [
        ("basic_case        ", [1, 1, 2], 2, [1, 2]),
        ("larger_array      ", [0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ("no_duplicates     ", [1, 2, 3], 3, [1, 2, 3]),
        ("all_same          ", [1, 1, 1, 1], 1, [1]),
        ("empty_array       ", [], 0, []),
        ("single_element    ", [1], 1, [1]),
    ],
)
def test_remove_duplicates(name, nums, expected_length, expected_nums):
    solution = Solution()
    length = solution.removeDuplicates(nums)
    assert length == expected_length
    assert nums[:length] == expected_nums, name
