"""
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can
only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on
them. Design an algorithm to find a path for the robot from the top left to the bottom right.
"""
import pytest


def find_path(grid):
    path = []
    failed_points = set()
    
    def find_path_helper(r, c):
        # Return if out of bounds or if cell is off limits
        if r < 0 or c < 0 or grid[r][c] or (r, c) in failed_points:
            return False
        
        # If there is a path from start to left or top cell add the current cell to the path
        if (r == 0 and c == 0) or find_path_helper(r - 1, c) or find_path_helper(r, c - 1):
            path.append((r, c))
            return True
        failed_points.add((r, c))
        return False
    
    return path if find_path_helper(len(grid) - 1, len(grid[0]) - 1) else []


@pytest.mark.parametrize('grid, path_expected', [
    ([[0, 0, 0, 0, 0, 0, 1],
      [0, 1, 1, 0, 1, 1, 0],
      [0, 0, 1, 0, 0, 0, 0],
      [1, 1, 0, 0, 0, 1, 0]],
     [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (2, 3), (2, 4), (2, 5), (2, 6), (3, 6)]),
    
    ([[0, 0, 0, 0, 0, 0, 1],
      [0, 1, 0, 1, 1, 1, 0],
      [0, 0, 0, 1, 0, 0, 0],
      [1, 1, 0, 0, 0, 1, 0]],
     [])
])
def test_find_path(grid, path_expected):
    assert find_path(grid) == path_expected
