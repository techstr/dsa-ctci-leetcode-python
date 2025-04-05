#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
from typing import List
import pytest


class Solution:
    """
    Given an integer rowIndex, return the rowIndex-th (0-indexed) row of Pascal's Triangle.

    Pascal's Triangle is a triangular array of integers where:
    - The first and last elements of each row are 1.
    - Each element in between is the sum of the two elements directly above it in the previous row.

    Args:
        rowIndex (int): The index of the row in Pascal's Triangle to return (0-indexed).

    Returns:
        List[int]: The rowIndex-th row of Pascal's Triangle as a list of integers.

    """

    # def getRow(self, rowIndex: int) -> List[int]:
    #     row = []
    #     for n in range(rowIndex + 1):
    #         prev = 1  # Start each row with 1
    #         for p in range(1, n):  # Calculate values between the first and last element
    #             temp = row[p]
    #             row[p] = prev + row[p]
    #             prev = temp
    #         row.append(1)  # End each row with 1 (except the first row)
    #     return row
    def getRow(self, rowIndex: int) -> List[int]:
        """
        1   1   1   1   1
        1   1   1   1   1
        1   1   1   2   1
        1   1   3   3   1
        1   4   6   4   1

        """
        row = [1] * (rowIndex + 1)  # Initialize the row with all 1s
        for n in range(1, rowIndex):  # Start from the second row
            for p in range(n, 0, -1):  # Update values from right to left
                row[p] += row[p - 1]
        return row


# @lc code=end


@pytest.mark.parametrize(
    "rowIndex, expected",
    [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
        (5, [1, 5, 10, 10, 5, 1]),
        (6, [1, 6, 15, 20, 15, 6, 1]),
    ],
)
def test_getRow(rowIndex, expected):
    solution = Solution()
    assert solution.getRow(rowIndex) == expected
