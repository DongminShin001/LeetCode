"""
25. Reverse Nodes in K-Group
Difficulty: Hard
Companies: Google, Meta

Problem:
Given the head of a linked list, reverse the nodes of the list k at a time
and return the modified list. k is a positive integer and at most equal to the
length of the list. If the number of nodes is not a multiple of k, the remaining
nodes at the end are left as-is. You may not alter the values in the list nodes.

Examples:

1. head = 1->2->3->4->5, k = 2
   Group 1: [1,2] -> reversed: 2->1
   Group 2: [3,4] -> reversed: 4->3
   Remainder: [5] -> left as-is: 5
   Answer: 2->1->4->3->5

2. head = 1->2->3->4->5, k = 3
   Group 1: [1,2,3] -> reversed: 3->2->1
   Remainder: [4,5] (less than k) -> left as-is: 4->5
   Answer: 3->2->1->4->5

3. head = 1->2->3->4->5, k = 1
   k=1 means no reversal needed; every group is a single node.
   Answer: 1->2->3->4->5

4. head = 1, k = 1
   Single node, nothing to reverse.
   Answer: 1

5. head = 1->2->3->4, k = 4
   Exactly one group of 4: [1,2,3,4] -> reversed: 4->3->2->1
   No remainder.
   Answer: 4->3->2->1
"""
