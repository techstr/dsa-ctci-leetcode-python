#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

from dataclasses import dataclass
from typing import List, Optional

import pytest


@dataclass
class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int): The value of the node.
        left (Optional[TreeNode]): The left child node.
        right (Optional[TreeNode]): The right child node.
    """

    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


# @lc code=start
class Solution:
    """
    Performs a postorder traversal of a binary tree.

    Args:
        root (Optional[TreeNode]): The root of the binary tree.

    Returns:
        List[int]: A list of node values in postorder sequence.
    """

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive approach.
        # if root is None:
        #     return []
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        # Iterative approach using a stack.
        if root is None:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result[::-1]  # Reverse the result to get postorder


# @lc code=end


@pytest.mark.parametrize(
    "level_order, expected",
    [  # Complex tree
        ([1, None, 2, 3], [3, 2, 1]),  # Right-skewed tree
        ([1, 2, None, 3], [3, 2, 1]),  # Left-skewed tree
        ([1, 2, 3, 4, 5, 6, 7], [4, 5, 2, 6, 7, 3, 1]),  # Complete binary tree
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 6, 7, 5, 2, 9, 8, 3, 1]),  # Complex tree
        ([], []),  # Empty tree
        ([1], [1]),  # Single node tree
    ],
)
def test_postorder_traversal(level_order, expected):
    root = level_order_array_to_tree(level_order)
    solution = Solution()
    assert solution.postorderTraversal(root) == expected


def level_order_array_to_tree(level_order: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Converts a level-order array representation of a binary tree to a TreeNode structure.

    Args:
        level_order (List[Optional[int]]): The level-order array representation of the binary tree.

    Returns:
        Optional[TreeNode]: The root of the binary tree.
    """
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = [root]
    i = 1

    while queue and i < len(level_order):
        current = queue.pop(0)
        if current:
            if i < len(level_order) and level_order[i] is not None:
                current.left = TreeNode(level_order[i])
                queue.append(current.left)
            i += 1
            if i < len(level_order) and level_order[i] is not None:
                current.right = TreeNode(level_order[i])
                queue.append(current.right)
            i += 1

    return root
