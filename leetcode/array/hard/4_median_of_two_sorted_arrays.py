#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List
import pytest


class Solution:
    """
    Finds the median of two sorted arrays.

    This method takes two sorted arrays as input and returns the median of the
    combined sorted array. The overall run time complexity should be O(log(min(m, n))),
    where m and n are the lengths of the two input arrays.

    Args:
        nums1 (List[int]): The first sorted array.
        nums2 (List[int]): The second sorted array.

    Returns:
        float: The median of the two sorted arrays.
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return 0.0


# @lc code=end


@pytest.mark.parametrize(
    "name, nums1, nums2, expected",
    [
        ("Odd total length  ", [1, 3], [2], 2.0),  # Odd total length
        ("Even total length ", [1, 2], [3, 4], 2.5),  # Even total length
        ("One array empty   ", [], [1], 1.0),  # One array is empty
        ("Other array empty ", [2], [], 2.0),  # Other array is empty
        ("All zeros         ", [0, 0], [0, 0], 0.0),  # All elements are zero
        ("Two sorted arrays ", [1, 2, 3], [4, 5, 6], 3.5),  # Two sorted arrays
        ("Mixed arrays      ", [1, 3], [2, 7], 2.5),  # Mixed arrays
        ("Interleaved arrays", [1, 2, 6], [3, 4, 5], 3.5),  # Interleaved arrays
    ],
)
def test_findMedianSortedArrays(name, nums1, nums2, expected):
    solution = Solution()
    assert solution.findMedianSortedArrays(nums1, nums2) == expected, name
