#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Generates Pascal's Triangle up to the given number of rows.

    Pascal's Triangle is a triangular array of integers where the value at
    each position is the sum of the two values directly above it in the
    previous row. The first and last values in each row are always 1.

    Args:
        numRows (int): The number of rows of Pascal's Triangle to generate.

    Returns:
        List[List[int]]: A list of lists, where each inner list represents
        a row of Pascal's Triangle.
    1
    1   1
    1   2   1
    1   3   3   1
    1   4   6   4   1
    1   5   10  10   5  1
    """

    # def generate(self, numRows: int) -> List[List[int]]:
    #     rows = []
    #     prevRow = []
    #     for n in range(numRows):
    #         r = 0
    #         row = []
    #         for p in range(n):
    #             row.append(r + prevRow[p])
    #             r = prevRow[p]
    #         row.append(1)
    #         prevRow = row
    #         rows.append(row)
    #     return rows

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        rows = []
        for n in range(numRows):
            row = [1]  # Start each row with 1
            for p in range(1, n):  # Calculate values between the first and last element
                row.append(rows[n - 1][p - 1] + rows[n - 1][p])
            if n > 0:
                row.append(1)  # End each row with 1 (except the first row)
            rows.append(row)
        return rows


# @lc code=end


@pytest.mark.parametrize(
    "numRows, expected",
    [
        (1, [[1]]),  # Single row
        (2, [[1], [1, 1]]),  # Two rows
        (3, [[1], [1, 1], [1, 2, 1]]),  # Three rows
        (4, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),  # Four rows
        (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),  # Five rows
    ],
)
def test_generate(numRows: int, expected: List[List[int]]):
    solution = Solution()
    assert solution.generate(numRows) == expected
