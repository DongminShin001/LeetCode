"""
#543 — Diameter of Binary Tree | Medium | Google, Meta

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter is the length of the longest path between any two nodes.
The path may or may not pass through the root.
Length = number of edges on the path.

---

Example 1:
  Tree:
      1
     / \\
    2   3
   / \\
  4   5

  Longest path: 4 → 2 → 1 → 3  or  5 → 2 → 1 → 3  (both length 3)
  At node 2: left depth = 1 (node 4), right depth = 1 (node 5) → path through 2 = 2
  At node 1: left depth = 2 (via node 2), right depth = 1 (node 3) → path through 1 = 3
  Output: 3

Example 2:
  Tree:
    1
   /
  2
  Longest path: 1 → 2, length 1.
  Output: 1

Example 3:
  Tree: single node 1
  No edges. Output: 0

Example 4:
  Tree (right-skewed):
    1
     \\
      2
       \\
        3
         \\
          4
  Longest path: 1→2→3→4, length 3.
  Output: 3

Example 5:
  Tree:
        1
       / \\
      2   3
     /     \\
    4       5
   /         \\
  6           7

  Path: 6→4→2→1→3→5→7, length 6.
  Output: 6

---

Constraints:
  - Number of nodes: [1, 10^4]
  - -100 <= Node.val <= 100
"""
