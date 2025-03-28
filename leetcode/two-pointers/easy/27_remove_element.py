#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
from typing import List
import pytest


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return 0


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
