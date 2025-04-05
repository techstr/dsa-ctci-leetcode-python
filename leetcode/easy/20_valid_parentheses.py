#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
import pytest


class Solution:
    """
    A class containing a method to determine if a string of parentheses is valid.

    Methods:
        isValid(s: str) -> bool:
            Determines if the input string `s` containing parentheses is valid.
            A string is considered valid if:
            - Open brackets are closed by the same type of brackets.
            - Open brackets are closed in the correct order.

    Args:
        s (str): A string containing only the characters '(', ')', '{', '}', '[' and ']'.

    Returns:
        bool: True if the string is valid, False otherwise.
    """

    def isValid(self, s: str) -> bool:
        """
        Approach:
        To solve this problem, you can use a stack data structure.
        The stack helps keep track of the open brackets,
        and you can match them with the closing brackets as you iterate through the string.

        Steps:
        Use a stack to store open brackets ((, {, [).
        Use a dictionary to map closing brackets to their corresponding open brackets.
        Iterate through the string:
            If the character is an open bracket, push it onto the stack.
        If the character is a closing bracket:
            Check if the stack is empty (invalid case).
            Pop the top of the stack and check if it matches the current closing bracket
            using the dictionary.
        After the loop, check if the stack is empty. If it's not, the string is invalid.
        """
        # Dictionary to map closing brackets to their corresponding opening brackets
        opposites = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            if char in opposites.values():  # If it's an opening bracket
                stack.append(char)
            elif char in opposites:  #' If it's a closing bracket
                # Check if stack is empty or top of stack doesn't match
                if not stack or stack.pop() != opposites[char]:
                    return False
            else:
                return False  # Invalid character (not a bracket)

        # If stack is empty, all brackets were matc'hed correctly
        return not stack


# @lc code=end


@pytest.mark.string
@pytest.mark.stack
@pytest.mark.parametrize(
    "s,expected",
    [
        ("", True),  # Empty string
        ("()", True),  # Simple valid parentheses
        ("()[]{}", True),  # Mixed valid parentheses
        ("(]", False),  # Mismatched parentheses
        ("([)]", False),  # Incorrectly nested
        ("{[]}", True),  # Correctly nested
        ("(", False),  # Single open parenthesis
        (")", False),  # Single close parenthesis
        ("{[(", False),  # Multiple open
        ("{[()]}", True),  # Complex valid
        ("{[()]}]", False),  # Extra closing
    ],
)
def testIsValid(s, expected):
    solution = Solution()
    assert solution.isValid(s) == expected
