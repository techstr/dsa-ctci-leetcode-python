#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

from collections import deque

# @lc code=start
import pytest


class MyStack:
    """
    A class to implement a stack using a single queue.

    Methods:
        __init__(): Initializes the stack.
        push(x: int): Pushes an element onto the stack.
        pop() -> int: Removes and returns the top element of the stack.
        top() -> int: Returns the top element of the stack without removing it.
        empty() -> bool: Checks if the stack is empty.
    """

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)
        # Rotate the queue to make the last element the front
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue


# Previous implementation using two queues (kept for reference)
# class MyStack:
#     def __init__(self):
#         self.queue = []
#
#     def push(self, x: int) -> None:
#         self.queue.append(x)
#
#     def pop(self) -> int:
#         if not self.queue:
#             return None
#         temp = []
#         while len(self.queue) > 1:
#             temp.append(self.queue.pop(0))
#         top_element = self.queue.pop(0)
#         self.queue = temp
#         return top_element
#
#     def top(self) -> int:
#         if not self.queue:
#             return None
#         temp = []
#         while len(self.queue) > 1:
#             temp.append(self.queue.pop(0))
#         top_element = self.queue.pop(0)
#         temp.append(top_element)
#         self.queue = temp
#         return top_element
#
#     def empty(self) -> bool:
#         return not self.queue


# @lc code=end


@pytest.mark.parametrize(
    "operations, values, expected",
    [
        (["push", "push", "top", "pop", "empty"], [[1], [2], [], [], []], [None, None, 2, 2, False]),
        (["push", "pop", "empty"], [[1], [], []], [None, 1, True]),
        (["empty"], [[]], [True]),
    ],
)
def test_my_stack(operations, values, expected):
    stack = MyStack()
    results = []
    for op, val in zip(operations, values):
        if op == "push":
            results.append(stack.push(*val))
        elif op == "pop":
            results.append(stack.pop())
        elif op == "top":
            results.append(stack.top())
        elif op == "empty":
            results.append(stack.empty())
    assert results == expected
