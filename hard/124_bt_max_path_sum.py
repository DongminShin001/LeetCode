"""
124. Binary Tree Maximum Path Sum
Difficulty: Hard
Companies: Google, Meta

Problem:
Given the root of a binary tree, return the maximum path sum of any non-empty path.
A path is a sequence of nodes where each pair of adjacent nodes has an edge.
A node can appear in the path at most once. The path does not need to pass through the root.
Node values can be negative.

Examples:

1. Tree:  1
         / \\
        2   3
   Path: 2 -> 1 -> 3  (sum = 6)
   Answer: 6

2. Tree:     -10
             /  \\
            9   20
               /  \\
              15   7
   Best path: 15 -> 20 -> 7  (sum = 42)
   The root -10 and node 9 are not included.
   Answer: 42

3. Tree:  -3
   Only one node, no choice.
   Answer: -3

4. Tree:    2
           / \\
          -1  3
   Paths: 2 alone=2, -1 alone=-1, 3 alone=3, -1->2=1, 2->3=5, -1->2->3=4
   Best: 2->3 = 5
   Answer: 5

5. Tree:      1
             / \\
            -2  -3
            / \\    \\
           1   3    -2
          /   /
         -1  -3
   Must pick the best sub-path, possibly just a single high-value node.
   Prune negative branches when they reduce the sum.
   Answer: 3   (the node with value 3 alone, since all extensions are negative)
"""
