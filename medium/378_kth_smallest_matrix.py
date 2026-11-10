"""
#378 — Kth Smallest Element in a Sorted Matrix | Medium | Google, Amazon

Given an n x n matrix where each row and column is sorted in non-decreasing order,
return the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

---

Example 1:
  Input:
    matrix = [[1, 5, 9],
              [10,11,13],
              [12,13,15]],
    k = 8
  Output: 13

  All elements sorted: [1,5,9,10,11,12,13,13,15]
  8th element (1-indexed) = 13.

Example 2:
  Input:  matrix = [[-5]], k = 1
  Output: -5

Example 3:
  Input:
    matrix = [[1,2],[1,3]], k = 2
  Sorted: [1,1,2,3]
  2nd element = 1.
  Output: 1

Example 4:
  Input:
    matrix = [[1, 3, 5],
              [6, 7, 12],
              [11,14,14]],
    k = 6
  Sorted: [1,3,5,6,7,11,12,14,14]
  6th element = 11.
  Output: 11

Example 5:
  Input:
    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12],
              [13,14,15,16]],
    k = 7
  Sorted: [1,2,3,4,5,6,7,8,9,...]
  7th element = 7.
  Output: 7

---

Constraints:
  - n == matrix.length == matrix[i].length
  - 1 <= n <= 300
  - -10^9 <= matrix[i][j] <= 10^9
  - All rows and columns are sorted in non-decreasing order.
  - 1 <= k <= n^2
  - Follow-up: can you solve it with O(n) memory?
"""
