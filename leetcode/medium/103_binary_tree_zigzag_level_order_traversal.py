#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
from dataclasses import dataclass
from typing import List, Optional

import pytest


# Definition for a binary tree node.
@dataclass
class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int): The value of the node.
        left (Optional[TreeNode]): The left child of the node.
        right (Optional[TreeNode]): The right child of the node.
    """

    val: int = 0
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


# @lc code=start
class Solution:
    """
    Performs a zigzag level order traversal of a binary tree.

    The traversal alternates between left-to-right and right-to-left order
    at each level of the tree.

    Args:
        root (Optional[TreeNode]): The root node of the binary tree.

    Returns:
        List[List[int]]: A list of lists, where each inner list contains the
        values of the nodes at a particular level of the tree, ordered
        according to the zigzag traversal pattern.
    """

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a zigzag level order traversal of a binary tree using stacks.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[List[int]]: A list of lists, where each inner list contains the
            values of the nodes at a particular level of the tree, ordered
            according to the zigzag traversal pattern.
        """
        if not root:
            return []

        result = []
        current_level = [root]
        left_to_right = True

        while current_level:
            level = []
            next_level = []

            for node in current_level:
                level.append(node.val)
                if left_to_right:
                    if node.left:
                        next_level.append(node.left)
                    if node.right:
                        next_level.append(node.right)
                else:
                    if node.right:
                        next_level.append(node.right)
                    if node.left:
                        next_level.append(node.left)

            result.append(level)
            current_level = next_level[::-1]
            left_to_right = not left_to_right

        return result


# @lc code=end


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


@pytest.mark.parametrize(
    "level_order, expected",
    [
        ([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]),
        ([1], [[1]]),
        ([], []),
        ([1, 2, 3, 4, 5, 6, 7], [[1], [3, 2], [4, 5, 6, 7]]),
        ([1, 2, None, 3, None, None, None], [[1], [2], [3]]),
    ],
)
def test_zigzag_level_order(level_order, expected):
    tree = level_order_array_to_tree(level_order)
    solution = Solution()
    assert solution.zigzagLevelOrder(tree) == expected
