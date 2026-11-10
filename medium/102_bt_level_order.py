"""
#102 — Binary Tree Level Order Traversal | Medium | Google, Amazon, Meta

Given the root of a binary tree, return the level order traversal of its nodes' values
as a list of lists — each inner list contains all node values at that depth, left to right.

---

Example 1:
  Input:
        3
       / \\
      9  20
        /  \\
       15   7

  Level 0: [3]
  Level 1: [9, 20]
  Level 2: [15, 7]
  Output: [[3],[9,20],[15,7]]

Example 2:
  Input:  root = [1]
  Output: [[1]]

Example 3:
  Input:  root = []
  Output: []

Example 4:
  Input:
      1
     / \\
    2   3
   / \\
  4   5

  Level 0: [1]
  Level 1: [2, 3]
  Level 2: [4, 5]
  Output: [[1],[2,3],[4,5]]

Example 5:
  Input:  (right-skewed tree)
    1
     \\
      2
       \\
        3
  Output: [[1],[2],[3]]

---

Constraints:
  - Number of nodes in the tree: [0, 2000]
  - -1000 <= Node.val <= 1000
"""
