#
# @lc app=leetcode id=1046 lang=python3
#
# [1046] Last Stone Weight
#

import heapq
from typing import List

import pytest


# @lc code=start
class Solution:
    """
    Class Solution:
        A class containing a method to solve the "Last Stone Weight" problem.

    Methods:
            Simulates the process of smashing stones together until at most one stone is left.

            Args:
                stones (List[int]): A list of integers representing the weights of the stones.

            Returns:
                int: The weight of the last remaining stone, or 0 if no stones are left.
    """

    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     while len(stones) > 1:
    #         stones.sort(reverse=True)
    #         first = stones.pop(0)
    #         second = stones.pop(0)
    #         if first != second:
    #             stones.append(first - second)
    #     return stones[0] if stones else 0

    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert stones to a max-heap by negating the values
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # Extract the two heaviest stones
            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            # If they are not equal, push the difference back into the heap
            if first != second:
                heapq.heappush(stones, -(first - second))

        # Return the last stone weight or 0 if no stones are left
        return -stones[0] if stones else 0


# @lc code=end


@pytest.mark.parametrize("stones, expected", [([2, 7, 4, 1, 8, 1], 1), ([1], 1), ([3, 3], 0), ([10, 4, 2, 10], 2), ([1, 1, 1, 1], 0)])
def test_last_stone_weight(stones, expected):
    solution = Solution()
    assert solution.lastStoneWeight(stones) == expected
