#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#


# @lc code=start
class MyQueue:
    """
    Implements a queue using two stacks.

    This class provides standard queue operations (`push`, `pop`, `peek`, `empty`)
    using two internal stacks to maintain FIFO order. The `push` operation adds
    elements to the input stack, while `pop` and `peek` transfer elements to the
    output stack as needed to reverse the order for correct queue behavior.
    """

    def __init__(self):
        # in_stack for incoming pushes, out_stack for pops/peeks
        self._in = []
        self._out = []

    def push(self, x: int) -> None:
        self._in.append(x)

    def pop(self) -> int:
        if not self._out:
            # Move all elements from in to out to reverse order
            while self._in:
                self._out.append(self._in.pop())
        return self._out.pop()

    def peek(self) -> int:
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        return self._out[-1]

    def empty(self) -> bool:
        return not self._in and not self._out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# @lc code=end

# --------------------
# PyTest unit tests
# --------------------
import pytest


@pytest.mark.parametrize(
    "ops,args,expected",
    [
        # Basic FIFO behavior with peek/empty checks
        (
            ["push", "push", "peek", "pop", "empty", "pop", "empty"],
            [[1], [2], [], [], [], [], []],
            [None, None, 1, 1, False, 2, True],
        ),
        # Interleaved push and pop
        (
            ["push", "pop", "empty"],
            [[42], [], []],
            [None, 42, True],
        ),
        # Multiple peeks shouldn't remove elements
        (
            ["push", "push", "peek", "peek", "pop", "peek", "empty"],
            [[3], [4], [], [], [], [], []],
            [None, None, 3, 3, 3, 4, False],
        ),
        # Larger sequence with more pushes after some pops
        (
            ["push", "push", "push", "push", "push", "pop", "pop", "pop", "push", "push", "pop", "pop", "pop", "peek", "empty"],
            [[1], [2], [3], [4], [5], [], [], [], [6], [7], [], [], [], [], []],
            [None, None, None, None, None, 1, 2, 3, None, None, 4, 5, 6, 7, False],
        ),
    ],
)
def test_myqueue_operations(ops, args, expected):
    q = MyQueue()
    actual = []
    for op, a in zip(ops, args):
        if op == "push":
            actual.append(q.push(*a))
        elif op == "pop":
            actual.append(q.pop())
        elif op == "peek":
            actual.append(q.peek())
        elif op == "empty":
            actual.append(q.empty())
        else:
            raise ValueError(f"Unknown op: {op}")
    assert actual == expected
