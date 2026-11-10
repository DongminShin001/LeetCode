"""
#235 — Lowest Common Ancestor of a Binary Search Tree | Medium | Google, Amazon

Given a BST and two nodes p and q, find their lowest common ancestor (LCA).
The LCA is the deepest node that has both p and q as descendants (a node is a descendant of itself).

BST property: for every node, left subtree values < node.val < right subtree values.
Use this ordering to navigate efficiently — no need to search both subtrees blindly.

---

Example 1:
  BST:
          6
         / \\
        2   8
       / \\ / \\
      0  4 7  9
        / \\
       3   5

  p=2, q=8 → LCA = 6
  At node 6: p(2) < 6 and q(8) > 6 → split here → LCA = 6

Example 2:
  Same BST.
  p=2, q=4 → LCA = 2
  At node 6: both < 6 → go left to node 2
  At node 2: p==2 → 2 is ancestor of 4 → LCA = 2

Example 3:
  Same BST.
  p=3, q=5 → LCA = 4
  At 6: both < 6 → go left to 2
  At 2: both > 2 → go right to 4
  At 4: p(3) < 4 and q(5) > 4 → split → LCA = 4

Example 4:
  BST:
    2
   / \\
  1   3

  p=1, q=3 → LCA = 2 (split at root)

Example 5:
  BST: single node 1, p=1, q=1
  LCA = 1

---

Constraints:
  - Number of nodes: [2, 10^5]
  - -10^9 <= Node.val <= 10^9
  - All Node.val are unique.
  - p != q
  - Both p and q exist in the BST.
"""
