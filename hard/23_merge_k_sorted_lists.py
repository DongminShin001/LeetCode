"""
23. Merge K Sorted Lists
Difficulty: Hard
Companies: Google, Amazon, Meta

Problem:
Given an array of k linked lists, each sorted in ascending order, merge all
the linked lists into one sorted linked list and return it.

Examples:

1. lists = [[1->4->5], [1->3->4], [2->6]]
   Compare heads: 1, 1, 2 — pick 1 (list 0)
   Compare heads: 4, 1, 2 — pick 1 (list 1)
   Compare heads: 4, 3, 2 — pick 2 (list 2)
   Continue until all exhausted.
   Answer: 1->1->2->3->4->4->5->6

2. lists = []
   No lists to merge.
   Answer: []

3. lists = [[]]
   Single empty list.
   Answer: []

4. lists = [[-1->0->1], [-3->-2,-2], [-1->1->2]]
   Merge all; smallest values first.
   Answer: -3->-2->-2->-1->-1->0->1->1->2

5. lists = [[1->2->3->4->5], [6->7->8->9->10]]
   No overlap between lists.
   First list is entirely less than second.
   Answer: 1->2->3->4->5->6->7->8->9->10
"""
