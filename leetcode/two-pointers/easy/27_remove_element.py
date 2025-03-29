#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List
import pytest


class Solution:
    """
    Given an integer array `nums` and an integer `val`, this method removes all occurrences of `val`
    in `nums` in-place.
    The relative order of the elements may be changed. It returns the number of elements in `nums`
    which are not equal to `val`.

    Args:
        nums (List[int]): The input list of integers.
        val (int): The value to be removed from the list.

    Returns:
        int: The number of elements remaining in the list after removing all occurrences of `val`.

    Note:
        - The function modifies the input list `nums` in-place.
        - The returned value represents the new length of the modified list.
    """

    # def removeElement(self, nums: List[int], val: int) -> int:
    #     if not nums:
    #         return 0
    #     write_loc = 0
    #     queue = []
    #     count = 0
    #     for i, n in enumerate(nums):
    #         if n == val:
    #             queue.append(i)
    #         else:
    #             count += 1
    #             if queue:
    #                 write_loc = queue.pop(0)
    #                 nums[write_loc] = n
    #                 queue.append(i)
    #     return count

    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        left = 0
        for num in nums:
            if num != val:
                nums[left] = num
                left += 1
        return left


# @lc code=end


@pytest.mark.parametrize(
    "name, nums, val, expected",
    [
        ("example_1         ", [3, 2, 2, 3], 3, 2),
        ("example_2         ", [0, 1, 2, 2, 3, 0, 4, 2], 2, 5),
        ("single_element_1  ", [1], 1, 0),
        ("no_removal_needed ", [4, 5], 6, 2),
        ("empty_list        ", [], 1, 0),
    ],
)
def test_remove_element(name, nums, val, expected):
    solution = Solution()
    result = solution.removeElement(nums, val)
    assert result == expected, name
