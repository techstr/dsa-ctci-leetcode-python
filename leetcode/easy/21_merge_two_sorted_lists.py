#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional

import pytest


class ListNode:
    """
    Represents a node in a singly linked list.

    Attributes:
        val (int): The value stored in the node. Defaults to 0.
        next (ListNode or None): A reference to the next node in the list. Defaults to None.
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Merge two sorted linked lists into a single sorted linked list.

    This function takes two sorted linked lists as input and merges them into a single
    sorted linked list. The resulting linked list is constructed by splicing together
    the nodes of the input lists.

    Args:
        list1 (Optional[ListNode]): The head of the first sorted linked list.
        list2 (Optional[ListNode]): The head of the second sorted linked list.

    Returns:
        Optional[ListNode]: The head of the merged sorted linked list. If both input
        lists are empty, returns None.
    """

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Complexity
        O(n + m):
        Here, n is the number of nodes in list1, and m is the number of nodes in list2.
        The algorithm iterates through both linked lists once, comparing their
        nodes and appending the smaller node to the merged list.
        This results in a linear traversal of all nodes in both lists.
        Space Complexity
        O(1):
        The solution uses a constant amount of extra space. It does not create new nodes but
        instead reuses the nodes from the input lists by rearranging their next pointers.
        The only additional space used is for the dummy node and a few pointers (dummy and current),
        which are constant in size.
        """
        # Create a dummy node to simplify edge cases
        dummy = ListNode(-1)
        current = dummy

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the remaining nodes from either list1 or list2
        current.next = list1 if list1 else list2

        # Return the merged list, skipping the dummy node
        return dummy.next


# @lc code=end


def list_to_linked_list(elements):
    """Helper function to convert a Python list to a linked list."""
    if not elements:
        return None
    head = ListNode(elements[0])
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(head):
    """Helper function to convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


@pytest.mark.parametrize(
    "name, list1, list2, expected",
    [
        ("Both empty    ", [], [], []),
        ("One empty 1   ", [1, 2, 4], [], [1, 2, 4]),
        ("One empty 2   ", [], [1, 3, 4], [1, 3, 4]),
        ("Non-empty     ", [1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ("Interleaved   ", [1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ("Duplicates    ", [1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
    ],
)
def test_merge_two_sorted_lists(name, list1, list2, expected):
    solution = Solution()
    l1 = list_to_linked_list(list1)
    l2 = list_to_linked_list(list2)
    merged_head = solution.mergeTwoLists(l1, l2)
    result = linked_list_to_list(merged_head)
    assert result == expected, name
