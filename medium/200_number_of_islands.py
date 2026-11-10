"""
#200 — Number of Islands | Medium | Google, Amazon, Meta

Given an m x n 2D binary grid where '1' represents land and '0' represents water,
return the number of islands. An island is surrounded by water and is formed by connecting
adjacent land cells horizontally or vertically.

---

Example 1:
  Input:
    grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
  Output: 1
  All '1' cells are connected — one large island.

Example 2:
  Input:
    grid = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
  Output: 3
  Island 1: top-left 2x2 block
  Island 2: single cell at (2,2)
  Island 3: two cells at (3,3) and (3,4)

Example 3:
  Input:
    grid = [["1"]]
  Output: 1

Example 4:
  Input:
    grid = [["0","0"],["0","0"]]
  Output: 0  (no land)

Example 5:
  Input:
    grid = [
      ["1","0","1"],
      ["0","1","0"],
      ["1","0","1"]
    ]
  Output: 5
  Each '1' is isolated (diagonal connections don't count).

---

Constraints:
  - m == grid.length
  - n == grid[i].length
  - 1 <= m, n <= 300
  - grid[i][j] is '0' or '1'
"""
