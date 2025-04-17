#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

import pytest


# @lc code=start
class Solution:
    """
    Class Solution contains a method to find the index of the first occurrence of a substring (needle) in a string (haystack).

    Methods:
        Finds the first occurrence of the substring `needle` in the string `haystack`.
        If `needle` is an empty string, returns 0.
        If `needle` is not found in `haystack`, returns -1.

        Args:
            haystack (str): The string to search within.
            needle (str): The substring to search for.

        Returns:
            int: The index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not found.
    """

    # def strStr(self, haystack: str, needle: str) -> int:
    #     return 0 if needle == "" else haystack.find(needle)

    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        haystack_len = len(haystack)
        needle_len = len(needle)

        for i in range(haystack_len - needle_len + 1):
            match = True
            for j in range(needle_len):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i

        return -1


# @lc code=end


@pytest.mark.parametrize(
    "haystack, needle, expected",
    [
        ("hello", "ll", 2),  # 'll' starts at index 2 in 'hello'
        ("aaaaa", "bba", -1),  # 'bba' is not in 'aaaaa'
        ("", "", 0),  # Empty needle in empty haystack returns 0
        ("a", "", 0),  # Empty needle in non-empty haystack returns 0
        ("a", "a", 0),  # Single character match
        ("mississippi", "issip", 4),  # 'issip' starts at index 4 in 'mississippi'
    ],
)
def test_strStr(haystack, needle, expected):
    solution = Solution()
    assert solution.strStr(haystack, needle) == expected
