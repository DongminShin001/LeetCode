"""
85. Maximal Rectangle
Difficulty: Hard
Companies: Google, Amazon

Problem:
Given a rows x cols binary matrix filled with '0's and '1's, find the largest
rectangle containing only '1's and return its area.

Examples:

1. matrix = [["1","0","1","0","0"],
             ["1","0","1","1","1"],
             ["1","1","1","1","1"],
             ["1","0","0","1","0"]]
   Build histogram row by row:
   Row 0 heights: [1,0,1,0,0]
   Row 1 heights: [2,0,2,1,1]
   Row 2 heights: [3,1,3,2,2]  <- largest rectangle here: width 5, min height 1? No.
                                   try heights [3,1,3,2,2]: largest bar histogram = 6
   Row 3 heights: [4,0,0,3,0]
   Answer: 6

2. matrix = [["0"]]
   All zeros, no rectangle of 1s.
   Answer: 0

3. matrix = [["1"]]
   Single 1, area = 1.
   Answer: 1

4. matrix = [["1","1"]]
   Heights: [1,1]. Largest rectangle: 1x2 = 2.
   Answer: 2

5. matrix = [["1","0","1"],
             ["1","1","1"],
             ["0","1","1"]]
   Row 0 heights: [1,0,1]
   Row 1 heights: [2,1,2]  <- histogram max area = 4 (the two 2s plus the 1 between = 1*3=3? or 2*2=4)
   Row 2 heights: [0,2,3]
   Answer: 4
"""
