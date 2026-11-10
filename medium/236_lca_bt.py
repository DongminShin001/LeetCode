"""
#236 — Lowest Common Ancestor of a Binary Tree | Medium | Google, Meta, Amazon

Given a binary tree and two nodes p and q, find their lowest common ancestor (LCA).
The LCA is the deepest node that has both p and q as descendants (a node is a descendant of itself).

The tree is not necessarily a BST — no ordering property can be used.

---

Example 1:
  Tree:
          3
         / \\
        5   1
       / \\ / \\
      6  2 0  8
        / \\
       7   4

  p=5, q=1 → LCA = 3
  Node 3 has 5 in left subtree and 1 in right subtree → 3 is the LCA.

Example 2:
  Same tree.
  p=5, q=4 → LCA = 5
  4 is a descendant of 5, and 5 is a descendant of itself → LCA = 5.

Example 3:
  Same tree.
  p=6, q=4 → LCA = 5
  6 is in left subtree of 5; 4 is in right subtree of 5 → LCA = 5.

Example 4:
  Tree:
      1
     / \\
    2   3

  p=2, q=3 → LCA = 1

Example 5:
  Tree: single node 1, p=1, q=1
  LCA = 1

---

Constraints:
  - Number of nodes: [2, 10^5]
  - -10^9 <= Node.val <= 10^9
  - All Node.val are unique.
  - p != q
  - Both p and q exist in the tree.
"""
