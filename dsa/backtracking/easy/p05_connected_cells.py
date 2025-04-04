import pytest


class Solution:
    """
    A class to find the largest connected region of 1s in a binary matrix using Depth-First Search (DFS).

    Attributes:
        matrix (list[list[int]]): The binary matrix where 1 represents a cell that is part of a region and 0 represents an empty cell.
        visited (list[list[bool]]): A matrix to keep track of visited cells during the DFS traversal.
        max_region_size (int): The size of the largest connected region found in the matrix.

    Methods:
        __init__(matrix):
            Initializes the Solution object with the given binary matrix and sets up the visited matrix.

        is_valid(x, y):
            Checks if a cell (x, y) is within bounds, has not been visited, and contains a 1.

        dfs(x, y):
            Performs a Depth-First Search (DFS) starting from cell (x, y) to calculate the size of the connected region.
    """

    def __init__(self, matrix):
        self.matrix = matrix
        self.visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.max_region_size = 0

    def is_valid(self, x, y):
        return 0 <= x < len(self.matrix) and 0 <= y < len(self.matrix[0]) and not self.visited[x][y] and self.matrix[x][y] == 1

    def dfs(self, x, y):
        # Directions for 8 possible moves (horizontal, vertical, diagonal)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        stack = [(x, y)]
        size = 0

        while stack:
            cx, cy = stack.pop()
            if not self.is_valid(cx, cy):
                continue
            self.visited[cx][cy] = True
            size += 1

            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if self.is_valid(nx, ny):
                    stack.append((nx, ny))

        return size


@pytest.mark.parametrize(
    "matrix, expected",
    [
        (
            [
                [0, 0, 1, 1, 0],
                [1, 1, 1, 0, 0],
                [0, 0, 1, 0, 1],
                [1, 0, 0, 1, 1],
            ],
            9,  # Largest region size
        ),
        (
            [
                [1, 1, 0, 0],
                [0, 1, 0, 1],
                [1, 0, 0, 1],
                [0, 0, 1, 1],
            ],
            4,  # Largest region size
        ),
        (
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0],
            ],
            0,  # No regions
        ),
        (
            [
                [1, 1],
                [1, 1],
            ],
            4,  # Single region covering the entire matrix
        ),
        (
            [
                [1],
            ],
            1,  # Single cell region
        ),
    ],
)
def test_largest_region(matrix, expected):
    solution = Solution(matrix)
    largest_region = 0

    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            if not solution.visited[i][j] and matrix[i][j] == 1:
                largest_region = max(largest_region, solution.dfs(i, j))

    assert largest_region == expected
