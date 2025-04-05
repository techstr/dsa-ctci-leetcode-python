#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    A class used to merge two sorted arrays into one sorted array in-place.
    Methods
    -------
    merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None
        Merges the sorted array nums2 into nums1 in-place, assuming nums1 has
        enough space to hold the additional elements.
        Merges two sorted arrays, nums1 and nums2, into a single sorted array in-place.
        Parameters
        ----------
        nums1 : List[int]
            The first sorted array, which has enough space to hold the elements of nums2.
            The first m elements represent the initialized part of nums1.
        m : int
            The number of initialized elements in nums1.
        nums2 : List[int]
            The second sorted array.
        n : int
            The number of elements in nums2.
        Returns
        -------
        None
            The function modifies nums1 in-place to contain the merged sorted array.
        Notes
        -----
        - The merging starts from the end of nums1 to avoid overwriting elements.
        - If nums2 has remaining elements after the main loop, they are copied into nums1.
    """

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start merging from the end of nums1
        p1 = m - 1  # Pointer for the last initialized element in nums1
        p2 = n - 1  # Pointer for the last element in nums2
        p = m + n - 1  # Pointer for the last position in nums1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them
        nums1[: p2 + 1] = nums2[: p2 + 1]


# @lc code=end


@pytest.mark.parametrize(
    "nums1, m, nums2, n, expected",
    [
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),  # Basic merge
        ([1], 1, [], 0, [1]),  # nums2 is empty
        ([0], 0, [1], 1, [1]),  # nums1 is empty
        ([2, 0], 1, [1], 1, [1, 2]),  # Single element merge
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),  # nums2 smaller
        ([1, 2, 4, 5, 6, 0], 5, [3], 1, [1, 2, 3, 4, 5, 6]),  # Insert in the middle
    ],
)
def test_merge(nums1, m, nums2, n, expected):
    solution = Solution()
    nums1_copy = nums1.copy()  # Create a copy of nums1 to avoid in-place modification issues
    nums2_copy = nums2.copy()
    solution.merge(nums1_copy, m, nums2_copy, n)
    assert nums1_copy == expected
