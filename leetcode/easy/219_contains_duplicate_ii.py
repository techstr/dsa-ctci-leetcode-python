#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Class Solution provides a method to determine if there are two distinct indices
    in an integer array such that the values at those indices are equal and the
    absolute difference between the indices is less than or equal to a given value.

    Methods:
        containsNearbyDuplicate(nums: List[int], k: int) -> bool:
            Checks if there exist two indices i and j in the array nums such that:
            - nums[i] == nums[j]
            - abs(i - j) <= k
            Returns True if such indices exist, otherwise False.

    Args:
        nums (List[int]): The input list of integers.
        k (int): The maximum allowed difference between the indices of duplicate values.

    Returns:
        bool: True if the conditions are met, otherwise False.
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Given an integer array nums and an integer k, return true if there are two distinct
        indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
        """
        # Create a dictionary to store the last index of each number
        index_map = {}

        for i, num in enumerate(nums):
            # If the number is already in the dictionary and the difference between the current
            #  index and the last index is less than or equal to k, return True
            if num in index_map and i - index_map[num] <= k:
                return True

            # Update the last index of the number
            index_map[num] = i

        return False


# @lc code=
@pytest.mark.array
@pytest.mark.hash_table
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 2, 3, 1], 3, True),  # Duplicate 1 within distance 3
        ([1, 0, 1, 1], 1, True),  # Duplicate 1 within distance 1
        ([1, 2, 3, 1, 2, 3], 2, False),  # No duplicates within distance 2
        ([1, 2, 3, 4, 5], 3, False),  # No duplicates at all
        ([1, 1], 1, True),  # Duplicate 1 within distance 1
        ([1], 1, False),  # Single element, no duplicates
        ([], 1, False),  # Empty list, no duplicates
        ([99, 99], 0, False),  # Duplicate 99 but distance is not <= k
    ],
)
def test_contains_nearby_duplicate(nums, k, expected):
    solution = Solution()
    assert solution.containsNearbyDuplicate(nums, k) == expected
