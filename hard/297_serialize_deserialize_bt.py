"""
297. Serialize and Deserialize Binary Tree
Difficulty: Hard
Companies: Google, Amazon, Meta

Problem:
Design an algorithm to serialize a binary tree to a string and deserialize
that string back to the original tree. There is no restriction on how the
serialization format is chosen, as long as serialize(deserialize(s)) == s
and the tree structure is preserved exactly.

Examples:

1. Tree:    1
           / \\
          2   3
             / \\
            4   5
   serialize  -> "1,2,#,#,3,4,#,#,5,#,#"  (preorder with null markers)
   deserialize -> reconstructs the same tree
   Output: [1,2,3,null,null,4,5]

2. Tree: empty (root = None)
   serialize  -> ""  or "#"
   deserialize -> None
   Output: []

3. Tree:    1
   serialize  -> "1,#,#"
   deserialize -> single node tree with value 1
   Output: [1]

4. Tree:  1
            \\
             2
              \\
               3
   serialize  -> "1,#,2,#,3,#,#"  (right-skewed)
   deserialize -> same right-skewed structure
   Output: [1,null,2,null,3]

5. Tree:      5
             / \\
            4   7
           /   / \\
          3   2   1
   serialize  -> "5,4,3,#,#,#,7,2,#,#,1,#,#"
   deserialize -> same structure restored
   The key invariant: deserialize(serialize(root)) produces identical tree.
"""
