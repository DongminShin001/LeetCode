"""
#572 — Subtree of Another Tree | Medium | Amazon, Meta

Given the roots of two binary trees root and subRoot, return true if there is a subtree
of root with the same structure and node values as subRoot. Otherwise return false.

A subtree of root is a node in root and all of its descendants.
root itself is considered a subtree of root.

---

Example 1:
  root:          subRoot:
      3              4
     / \\            / \\
    4   5           1   2
   / \\
  1   2

  At node 4 in root: matches subRoot exactly → True
  Output: True

Example 2:
  root:          subRoot:
      3              4
     / \\            / \\
    4   5           1   2
   / \\
  1   2
       \\
        0

  Node 4 in root has an extra child (0), doesn't match subRoot → False
  Output: False

Example 3:
  root = [1,1], subRoot = [1]
  root:    subRoot:
    1          1
   /
  1

  At root node 1: root has a left child, subRoot doesn't → not same structure
  At left child 1: matches subRoot (leaf node 1) → True
  Output: True

Example 4:
  root = [1,2,3], subRoot = [2]
  Subtree rooted at node 2 in root matches subRoot.
  Output: True

Example 5:
  root = [1], subRoot = [2]
  Only one node in root (val=1), subRoot has val=2 → no match.
  Output: False

---

Constraints:
  - Number of nodes in root: [1, 2000]
  - Number of nodes in subRoot: [1, 1000]
  - -10^4 <= Node.val <= 10^4
"""
