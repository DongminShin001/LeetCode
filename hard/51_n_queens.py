"""
51. N-Queens
Difficulty: Hard
Companies: Google

Problem:
Given an integer n, return all distinct solutions to the n-queens puzzle.
Place n queens on an n x n chessboard so that no two queens attack each other.
Queens attack along the same row, column, or diagonal.
Each solution is a list of strings where 'Q' marks a queen and '.' marks an empty cell.

Examples:

1. n = 4
   Solution 1:        Solution 2:
   . Q . .            . . Q .
   . . . Q            Q . . .
   Q . . .            . . . Q
   . . Q .            . Q . .
   Answer: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]

2. n = 1
   Only one cell; place the queen there.
   Answer: [["Q"]]

3. n = 2
   No valid placement for 2 queens on 2x2 board.
   Answer: []

4. n = 3
   No valid placement for 3 queens on 3x3 board.
   Answer: []

5. n = 5
   There are 10 distinct solutions for n=5.
   Example solution: Q....  /  ..Q..  /  ....Q  /  .Q...  /  ...Q.
   Answer: (10 total solutions)
"""
