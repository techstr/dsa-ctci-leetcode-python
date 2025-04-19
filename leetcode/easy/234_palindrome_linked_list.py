#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#


from dataclasses import dataclass

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

import pytest


@dataclass
class ListNode:
    """
    A class representing a node in a singly linked list.

    Attributes:
        val (int): The value stored in the node. Defaults to 0.
        next (Optional[ListNode]): A reference to the next node in the linked list. Defaults to None.
    """

    val: int = 0
    next: Optional["ListNode"] = None


class Solution:
    """
    Determines if a singly linked list is a palindrome.

    A palindrome is a sequence that reads the same backward as forward.
    This function checks whether the given linked list satisfies this condition.

    Args:
        head (Optional[ListNode]): The head node of the singly linked list.

    Returns:
        bool: True if the linked list is a palindrome, False otherwise.
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        My first attempt would be to convert to an array and then run the classic palindrome logic on it
        Time : O(n)
        Space : O(n) because of additional array

        How could I optimize to avoid the additional array?
        1. Reverse the linked list and then iterate through both to check if the values are matching --> Additional linked list
        2. Reverse only second half of the linked list and then compare both halfs
        """
        # Handle endge case, constraint says head is not empty, so not necessary
        # if not head:
        #     return True

        slow, fast, prev = head, head, None

        # Iterate two pointers fast and slow.
        # When fast reach end of LL, slow will be at the half way
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        prev, slow = slow, slow.next
        prev.next = None

        # Reverse the second half of LL
        while slow:
            slow.next, prev, slow = prev, slow, slow.next

        # Point fast to head and slow at the head of reversed LL (prev)
        fast, slow = head, prev

        # Pass fast and slow pointers in two halfs of LL and compare values
        while fast and slow:
            if fast.val != slow.val:
                return False
            fast, slow = fast.next, slow.next
        return True


# @lc code=end


def list_to_linked_list(numbers):
    """Helper function to convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy.next


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 2, 1], True),  # Palindrome linked list
        ([1, 2], False),  # Not a palindrome
        ([1, 2, 3, 2, 1], True),  # Palindrome linked list with odd length
        ([1], True),  # Single element is always a palindrome
    ],
)
def test_isPalindrome(nums, expected):
    solution = Solution()
    nums = list_to_linked_list(nums)
    assert solution.isPalindrome(nums) == expected
