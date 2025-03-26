#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List

import pytest


class Solution:
    """
    Class to solve the problem of finding the longest common prefix among a list of strings.

    Methods:
        longestCommonPrefix(strs: List[str]) -> str:
            Finds the longest common prefix string amongst an array of strings.
            If there is no common prefix, returns an empty string.

    Args:
        strs (List[str]): A list of strings to analyze for the longest common prefix.

    Returns:
        str: The longest common prefix shared among the input strings, 
        or an empty string if none exists.
    """
    # def longestCommonPrefix(self, strs: List[str]) -> str:
    #     """
    #     Time Complexity: O(n * m)
    #     n: Length of the first string (strs[0]).
    #     m: Number of strings in the list (len(strs)).
    #     For each character in the first string, the algorithm compares it with all other strings.
    #     Space Complexity: O(1) (no additional data structures are used).
    #     """
    #     if not strs:  # Handle the case where the list is empty
    #         return ""

    #     prefix = ""
    #     n = len(strs[0])  # Length of the first string
    #     m = len(strs)  # Number of strings in the list

    #     for i in range(n):  # Loop through characters of the first string
    #         char = strs[0][i]  # Current character to compare
    #         for j in range(m):  # Loop through all strings
    #             if i >= len(strs[j]) or strs[j][i] != char:  # Check bounds and mismatch
    #                 return prefix  # Return the prefix if mismatch or end of string
    #         prefix += char  # If inner loop completes, add the character to the prefix

    #     return prefix


    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Time Complexity: O(S)
        S: Total number of characters across all strings.
        Each character is compared at most once, making it more efficient than the current solution.
        Space Complexity: O(1) (no additional data structures are used).
        """
        if not strs:  # Handle the case where the list is empty
            return ""

        # Start with the first string as the prefix
        prefix = strs[0]

        # Compare the prefix with each string in the list
        for s in strs[1:]:
            # Reduce the prefix until it matches the start of the current string
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix
                if not prefix:  # If the prefix becomes empty, return ""
                    return ""
        return prefix


# @lc code=end


@pytest.mark.parametrize(
    "strs, expected",
    [
        (["flower", "flow", "flight"], "fl"),  # Common prefix exists
        (["dog", "racecar", "car"], ""),       # No common prefix
        (["interspecies", "interstellar", "interstate"], "inters"),  # Long common prefix
        (["a"], "a"),                          # Single string
        (["", "b"], ""),                       # One string is empty
        (["c", "c"], "c"),                     # Identical strings
        (["prefix", "prefixes", "prefixation"], "prefix"),  # Prefix is the entire first string
        (["abc", "abcd", "ab"], "ab"),         # Partial match
        ([], ""),                              # Empty list
    ],
)
def testLongestCommonPrefix(strs, expected):
    solution = Solution()
    assert solution.longestCommonPrefix(strs) == expected
