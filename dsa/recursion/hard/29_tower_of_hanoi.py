from typing import List

import pytest


class Solution:
    """
    Solves the Tower of Hanoi problem for `n` disks.

    The Tower of Hanoi is a mathematical puzzle
    where you have three rods and `n` disks of different sizes
    that can slide onto any rod. The puzzle starts with
    the disks stacked in ascending order of size on
    one rod (the source rod), with the smallest disk on top.
    The objective is to move the entire stack
    to another rod (the destination rod), obeying the following rules:
    1. Only one disk can be moved at a time.
    2. Each move consists of taking the upper disk from one of the stacks
        and placing it on top of another stack.
    3. No larger disk may be placed on top of a smaller disk.

    Args:
        n (int): The number of disks to move.
        from_peg (List[int]): The source peg represented as a list of integers, where each integer
                              corresponds to the size of a disk.
        to_peg (List[int]): The destination peg represented as a list of integers.
        aux_peg (List[int]): The auxiliary peg represented as a list of integers.

    Returns:
        None: The function modifies the pegs in place to represent
        the solution to the Tower of Hanoi problem.
    """

    def tower_of_hanoi(self, n: int, from_peg: List[int], to_peg: List[int], aux_peg: List[int]):
        if n == 1:
            # Base case: Move the single disk from source to destination
            to_peg.append(from_peg.pop())
            return

        # Step 1: Move n-1 disks from source to auxiliary peg
        self.tower_of_hanoi(n - 1, from_peg, aux_peg, to_peg)

        # Step 2: Move the nth disk from source to destination peg
        to_peg.append(from_peg.pop())

        # Step 3: Move the n-1 disks from auxiliary peg to destination peg
        self.tower_of_hanoi(n - 1, aux_peg, to_peg, from_peg)


@pytest.mark.parametrize(
    "n, from_peg, to_peg, aux_peg, expected_to_peg",
    [
        (1, [1], [], [], [1]),  # Single disk
        (2, [2, 1], [], [], [2, 1]),  # Two disks
        (3, [3, 2, 1], [], [], [3, 2, 1]),  # Three disks
    ],
)
def test_tower_of_hanoi(n, from_peg, to_peg, aux_peg, expected_to_peg):
    solution = Solution()
    solution.tower_of_hanoi(n, from_peg, to_peg, aux_peg)
    assert to_peg == expected_to_peg
