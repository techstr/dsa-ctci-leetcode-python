#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# Definition for a binary tree node.
from dataclasses import dataclass
from typing import List, Optional

import pytest


@dataclass
class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int): The value of the node. Defaults to 0.
        left (Optional[TreeNode]): The left child of the node. Defaults to None.
        right (Optional[TreeNode]): The right child of the node. Defaults to None.
    """

    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


# @lc code=start


class Solution:
    """
    A class used to perform preorder traversal of a binary tree.

    Methods
    -------
    preorderTraversal(root: Optional[TreeNode]) -> List[int]
        Returns a list of integers representing the preorder traversal
        of the binary tree rooted at 'root'.

    Perform a preorder traversal of a binary tree.

    Parameters
    ----------
    root : Optional[TreeNode]
        The root node of the binary tree. It can be None if the tree is empty.

    Returns
    -------
    List[int]
        A list of integers representing the values of the nodes visited
        in preorder (root, left, right) order.
    """

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive approach
        # result = []

        # def traverse(node):
        #     if node:
        #         result.append(node.val)
        #         traverse(node.left)
        #         traverse(node.right)

        # traverse(root)
        # return result

        # Iterative approach
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result


# @lc code=end


@pytest.mark.parametrize(
    "level_order, expected",
    [
        ([1, None, 2, 3], [1, 2, 3]),  # Example from LeetCode
        ([], []),  # Empty tree
        ([1], [1]),  # Single node tree
        ([1, 2, 3], [1, 2, 3]),  # Full binary tree
        ([1, None, 2, None, 3], [1, 2, 3]),  # Right-skewed tree
        ([1, 2, None, 3], [1, 2, 3]),  # Left-skewed tree
        ([1, 2, 3, 4, 5, 6, 7], [1, 2, 4, 5, 3, 6, 7]),  # Complete binary tree
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [1, 2, 4, 5, 6, 7, 3, 8, 9]),  # Complex tree
    ],
)
def test_preorder_traversal(level_order, expected):
    root = level_order_array_to_tree(level_order)
    solution = Solution()
    assert solution.preorderTraversal(root) == expected


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
