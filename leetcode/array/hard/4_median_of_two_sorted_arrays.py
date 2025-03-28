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

    1,3,5   2,4,6
    3,5     2,4
    3       4
    3.5


    1,3,6,7    2,8
    3,6,7      2
    3,6
    4.5

    1,2,3,4,6,7,8,9,10    5
    2,3,4,6,7,8,9,10

    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array for binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            partitionX = (low + high) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minX = float("inf") if partitionX == x else nums1[partitionX]

            maxY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minY = float("inf") if partitionY == y else nums2[partitionY]

            if maxX <= minY and maxY <= minX:
                if (x + y) % 2 == 0:
                    return (max(maxX, maxY) + min(minX, minY)) / 2
                else:
                    return max(maxX, maxY)
            elif maxX > minY:
                high = partitionX - 1
            else:
                low = partitionX + 1
        raise ValueError("Input arrays are not sorted.")


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
