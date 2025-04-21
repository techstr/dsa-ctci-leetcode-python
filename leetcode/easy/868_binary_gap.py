#
# @lc app=leetcode id=868 lang=python3
#
# [868] Binary Gap
#

import pytest


# @lc code=start
class Solution:
    """
    A class containing a method to calculate the maximum distance between two
    consecutive 1's in the binary representation of a given integer.

    Methods:
        binaryGap(n: int) -> int:
            representation of the input integer n. If there are fewer than two 1's,
            the method returns 0.

            Parameters:
                n (int): The input integer whose binary representation is analyzed.

            Returns:
                int: The maximum distance between two consecutive 1's in the binary
                representation of n, or 0 if there are fewer than two 1's.
    """

    def binaryGap(self, n: int) -> int:
        """
        Calculate the maximum distance between two consecutive 1's in the binary
        representation of n. If there are fewer than two 1's, return 0.
        """
        binary = bin(n)[2:]  # Convert to binary string
        last_index = -1
        max_gap = 0

        for i, bit in enumerate(binary):
            if bit == "1":
                if last_index != -1:
                    max_gap = max(max_gap, i - last_index)
                last_index = i

        return max_gap


# @lc code=end


@pytest.mark.parametrize(
    "n, expected",
    [
        (22, 2),  # Binary: 10110, max gap is 2
        (5, 2),  # Binary: 101, max gap is 2
        (6, 1),  # Binary: 110, max gap is 1
        (8, 0),  # Binary: 1000, fewer than two 1's
        (1, 0),  # Binary: 1, fewer than two 1's
        (9, 3),  # Binary: 1001, max gap is 3
    ],
)
def test_binary_gap(n, expected):
    solution = Solution()
    assert solution.binaryGap(n) == expected
