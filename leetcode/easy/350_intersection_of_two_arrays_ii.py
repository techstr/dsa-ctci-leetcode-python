#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    A class to solve the problem of finding the intersection of two arrays.

    Methods
    -------
    intersect(nums1: List[int], nums2: List[int]) -> List[int]:
        Finds the intersection of two integer arrays, ensuring that each element
        in the result appears as many times as it shows in both arrays.
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Finds the intersection of two sorted integer arrays.

        Parameters
        ----------
        nums1 : List[int]
            The first list of integers.
        nums2 : List[int]
            The second list of integers.

        Returns
        -------
        List[int]
            A list containing the intersection of the two input arrays, with each
            element appearing as many times as it shows in both arrays. Duplicate
            elements in the result are avoided.
        """
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result


# @lc code=end


@pytest.mark.parametrize(
    "nums1, nums2, expected",
    [
        ([1, 2, 2, 1], [2, 2], [2, 2]),  # Common elements are [2, 2]
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),  # Common elements are [4, 9]
        ([1, 2, 3], [4, 5, 6], []),  # No common elements
        ([], [1, 2, 3], []),  # One array is empty
        ([1, 2, 3], [], []),  # Other array is empty
        ([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]),  # All elements are the same
    ],
)
def test_intersection(nums1, nums2, expected):
    solution = Solution()
    assert sorted(solution.intersect(nums1, nums2)) == sorted(expected)
