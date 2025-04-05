from typing import Optional

import pytest

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    """
    Represents a node in a singly linked list.

    Attributes:
        val (int): The value stored in the node. Defaults to 0.
        next (ListNode or None): A reference to the next node in the linked list. Defaults to None.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Adds two numbers represented by linked lists.

    Each linked list represents a non-negative integer in reverse order, where each node contains a single digit.
    The function adds the two numbers and returns the sum as a linked list in the same reverse order format.

    Args:
        l1 (Optional[ListNode]): The head of the first linked list.
        l2 (Optional[ListNode]): The head of the second linked list.

    Returns:
        Optional[ListNode]: The head of the resulting linked list representing the sum of the two numbers.
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current = head
        carry = 0
        while l1 or l2 or carry:
            # Get the values of the current nodes, or 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10

            # Create a new node with the digit value and attach it to the result list
            current.next = ListNode(total % 10)
            current = current.next

            # Move to the next nodes in the input lists
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        # Return the next node of the dummy head, which is the actual head of the result list
        return head.next


# @lc code=end


def list_to_linked_list(numbers):
    """Helper function to convert a list to a linked list."""
    dummy = ListNode()
    current = dummy
    for number in numbers:
        current.next = ListNode(number)
        current = current.next
    return dummy.next


def linked_list_to_list(node):
    """Helper function to convert a linked list to a list."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


@pytest.mark.linked_list
@pytest.mark.math
@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),  # 342 + 465 = 807
        ([0], [0], [0]),  # 0 + 0 = 0
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),  # 9999999 + 9999 = 10009998
    ],
)
def test_add_two_numbers(l1, l2, expected):
    solution = Solution()
    l1_linked = list_to_linked_list(l1)
    l2_linked = list_to_linked_list(l2)
    result = solution.addTwoNumbers(l1_linked, l2_linked)
    assert linked_list_to_list(result) == expected
