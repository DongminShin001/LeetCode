"""
#1091 — Shortest Path in Binary Matrix | Medium | Google

Given an n x n binary matrix grid, return the length of the shortest clear path from
top-left (0,0) to bottom-right (n-1, n-1). A clear path only goes through cells with
value 0, moving in any of the 8 directions (horizontally, vertically, or diagonally).
Return -1 if no such path exists.
Path length = number of cells visited (including start and end).

---

Example 1:
  Input:  grid = [[0,1],[1,0]]
  Output: 2
  Path: (0,0) → (1,1) diagonally. Length = 2.

Example 2:
  Input:
    grid = [[0,0,0],
            [1,1,0],
            [1,1,0]]
  Output: 4
  Path: (0,0)→(0,1)→(0,2)→(1,2)→(2,2)? That's 5 cells.
  Shorter diagonal: (0,0)→(0,1)→(1,2)→(2,2) = 4 cells.

Example 3:
  Input:  grid = [[1,0,0],[1,1,0],[1,1,0]]
  Output: -1
  Start cell (0,0) = 1 → blocked immediately.

Example 4:
  Input:  grid = [[0]]
  Output: 1
  Already at destination.

Example 5:
  Input:
    grid = [[0,0,0],
            [0,0,0],
            [0,0,0]]
  Shortest path: (0,0)→(1,1)→(2,2) diagonally. Length = 3.
  Output: 3

---

Constraints:
  - n == grid.length == grid[i].length
  - 1 <= n <= 100
  - grid[i][j] is 0 or 1
"""
