from typing import List
import pytest


class Solution:
    """
    A class used to represent a solution to a specific problem.
    Methods
    -------
    method(input_data: List[int]) -> bool
        Determines a boolean result based on the provided input data.
    """

    def method(self, input_data: List[int]) -> bool:
        return True if input_data else False


@pytest.mark.parametrize(
    "input_data, expected_output",
    [
        ([1, 2, 3], True),
        ([4, 5, 6], True),
    ],
)
def test_method(input_data, expected_output):
    solution = Solution()
    assert solution.method(input_data) == expected_output
