#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Finds the majority element in a list of integers.

    The majority element is the element that appears more than ⌊n / 2⌋ times,
    where n is the size of the list. It is guaranteed that the majority element
    always exists in the input list.

    Args:
        nums (List[int]): A list of integers.

    Returns:
        int: The majority element in the list.
    """

    ## Best solution Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]  # Initialize with first element since list is guaranteed non-empty
        count = 1

        # Phase 1: Find a candidate for the majority element
        for num in nums[1:]:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Phase 2: Verify the candidate (optional if the problem guarantees a majority element)
        return candidate

    # # Brute-force approach
    # def majorityElement(self, nums: List[int]) -> int:
    #     memoize = {}
    #     for num in nums:
    #         memoize[num] = memoize[num] + 1 if num in memoize else 1
    #     max_num = nums[0]
    #     for key, value in memoize.items():
    #         if value > memoize[max_num]:
    #             max_num = key
    #     return max_num

    ## Divide-and-conquer approach
    # def majorityElement(self, nums: List[int]) -> int:
    #     def majority_element_rec(start, end):
    #         # Base case: only one element
    #         if start == end:
    #             return nums[start]

    #         # Divide the array into two halves
    #         mid = (start + end) // 2
    #         left_majority = majority_element_rec(start, mid)
    #         right_majority = majority_element_rec(mid + 1, end)

    #         # If both halves agree on the majority element
    #         if left_majority == right_majority:
    #             return left_majority

    #         # Count each element in the current range
    #         left_count = sum(1 for i in range(start, end + 1) if nums[i] == left_majority)
    #         right_count = sum(1 for i in range(start, end + 1) if nums[i] == right_majority)

    #         # Return the element with the higher count
    #         return left_majority if left_count > right_count else right_majority

    #     return majority_element_rec(0, len(nums) - 1)

    ## Bit-manipulation approach
    # def majorityElement(self, nums: List[int]) -> int:
    #     # Bit manipulation approach
    #     n = len(nums)
    #     majority = 0

    #     for i in range(32):  # Iterate over all 32 bits of an integer
    #         bit_count = 0
    #         for num in nums:
    #             # Count how many numbers have the i-th bit set
    #             if (num >> i) & 1:
    #                 bit_count += 1

    #             # If more than half of the numbers have the i-th bit set, set it in the result
    #             if bit_count > n // 2:
    #                 majority |= 1 << i

    #     # Handle negative numbers (Python uses signed integers)
    #     if majority >= (1 << 31):
    #         majority -= 1 << 32

    #     return majority


# @lc code=end


@pytest.mark.array
@pytest.mark.divide_and_conquer
@pytest.mark.bit_manipulation
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([3, 2, 3], 3),  # Test case 1: Majority element is 3
        ([2, 2, 1, 1, 1, 2, 2], 2),  # Test case 2: Majority element is 2
        ([1], 1),  # Test case 3: Single element list
        ([5, 5, 5, 1, 2, 5, 5], 5),  # Test case 4: Majority element is 5
        ([10, 10, 10, 10, 3, 4, 10], 10),  # Test case 5: Majority element is 10
    ],
)
def test_majority_element(nums, expected):
    solution = Solution()
    assert solution.majorityElement(nums) == expected
