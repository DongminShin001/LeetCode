"""
#104 — Maximum Depth of Binary Tree | Easy | Companies: Amazon, Apple, Google, LinkedIn (Everywhere)

Given the root of a binary tree, return its maximum depth.
Maximum depth is the number of nodes along the longest path from the root down to the farthest leaf.

Examples:
  root = [3, 9, 20, null, null, 15, 7]  ->  3
        3
       / \
      9  20
         / \
        15   7

  root = [1, null, 2]                   ->  2
  root = []                             ->  0
  root = [1]                            ->  1
  root = [1, 2, 3, 4, 5]               ->  3
        1
       / \
      2   3
     / \
    4   5

Constraints:
  - Number of nodes is in range [0, 10^4]
  - -100 <= Node.val <= 100
"""
