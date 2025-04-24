#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

from typing import List, Optional

# @lc code=start
# Definition for a binary tree node.
import pytest


class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int): The value of the node. Defaults to 0.
        left (TreeNode, optional): The left child of the node. Defaults to None.
        right (TreeNode, optional): The right child of the node. Defaults to None.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Performs an inorder traversal of a binary tree.

    Args:
        root (Optional[TreeNode]): The root node of the binary tree.

    Returns:
        List[int]: A list of integers representing the inorder traversal of the tree.
    """

    # def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    #     """
    #     Performs an inorder traversal of a binary tree using recursion.

    #     Args:
    #         root (Optional[TreeNode]): The root node of the binary tree.

    #     Returns:
    #         List[int]: A list of integers representing the inorder traversal of the tree.
    #     """

    #     def traverse(node: Optional[TreeNode], result: List[int]) -> None:
    #         if not node:
    #             return
    #         # Traverse the left subtree
    #         traverse(node.left, result)
    #         # Process the current node
    #         result.append(node.val)
    #         # Traverse the right subtree
    #         traverse(node.right, result)

    #     result = []
    #     traverse(root, result)
    #     return result

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an inorder traversal of a binary tree using a stack.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
            List[int]: A list of integers representing the inorder traversal of the tree.
        """
        result = []
        stack = []
        current = root

        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left

            # Process the node
            current = stack.pop()
            result.append(current.val)

            # Traverse to the right node
            current = current.right

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
        ([1, None, 2, 3], [1, 3, 2]),
        ([1], [1]),
        ([], []),
        ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, None, 3], [3, 2, 1]),
    ],
)
def test_inorder_traversal(level_order, expected):
    tree = level_order_array_to_tree(level_order)
    solution = Solution()
    assert solution.inorderTraversal(tree) == expected
