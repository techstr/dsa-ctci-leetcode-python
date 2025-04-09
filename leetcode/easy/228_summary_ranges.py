#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Given a sorted unique integer array `nums`, this method returns the smallest sorted list of ranges
    that cover all the numbers in the array exactly. Each range `[a, b]` in the list should be output
    as:

    - "a->b" if a != b
    - "a" if a == b

    Args:
        nums (List[int]): A sorted list of unique integers.

    Returns:
        List[str]: A list of strings representing the ranges.
    """

    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        Generates a list of summary ranges from a sorted unique integer array.

        Each range is represented as:
        - "a->b" if the range includes more than one number.
        - "a" if the range includes only one number.

        Args:
            nums (List[int]): A sorted list of unique integers.

        Returns:
            List[str]: A list of strings representing the ranges.

        Time Complexity:
            O(n): We iterate through the list once to generate the ranges.

        Space Complexity:
            O(1): Additional space usage is minimal, excluding the output list.
        """
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                # Add the range to the list
                ranges.append(f"{start}->{nums[i - 1]}" if start != nums[i - 1] else f"{start}")
                start = nums[i]

        # Add the last range
        ranges.append(f"{start}->{nums[-1]}" if start != nums[-1] else f"{start}")

        return ranges


# @lc code=end


@pytest.mark.array
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([0, 1, 2, 4, 5, 7], ["0->2", "4->5", "7"]),
        ([0, 2, 3, 4, 6, 8, 9], ["0", "2->4", "6", "8->9"]),
        ([], []),
        ([-1], ["-1"]),
        ([0], ["0"]),
        ([0, 1], ["0->1"]),
        ([0, 2], ["0", "2"]),
    ],
)
def test_summary_ranges(nums, expected):
    solution = Solution()
    assert solution.summaryRanges(nums) == expected
