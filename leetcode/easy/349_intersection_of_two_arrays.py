#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

from typing import List

# @lc code=start
import pytest


class Solution:
    """
    Class Solution provides a method to find the intersection of two arrays.

    Methods:
        intersection(nums1: List[int], nums2: List[int]) -> List[int]:
            Given two integer arrays nums1 and nums2, this method returns a list
            containing their intersection. Each element in the result must be unique,
            and the result can be returned in any order.
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Approach 2:
            Use Python's set intersection operation to find the common elements
            between two arrays. This approach is concise and efficient.
            Time Complexity: O(n+m)
            Space Complexity: O(n+m)

            # return list(set(nums1).intersection(set(nums2)))

        Approach 3:
            Use the two-pointer technique on sorted arrays to find the intersection.
            This avoids additional set operations and works efficiently for sorted arrays.
            Time Complexity: O(n log n + m log m) (due to sorting)
            Space Complexity: O(1) (excluding the output list)

        """

        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                if not result or result[-1] != nums1[i]:  # Avoid duplicates
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
        ([1, 2, 2, 1], [2, 2], [2]),  # Common elements are [2]
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),  # Common elements are [4, 9]
        ([1, 2, 3], [4, 5, 6], []),  # No common elements
        ([], [1, 2, 3], []),  # One array is empty
        ([1, 2, 3], [], []),  # Other array is empty
        ([1, 1, 1, 1], [1, 1, 1, 1], [1]),  # All elements are the same
    ],
)
def test_intersection(nums1, nums2, expected):
    solution = Solution()
    assert sorted(solution.intersection(nums1, nums2)) == sorted(expected)
