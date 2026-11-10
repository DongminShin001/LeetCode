"""
#21 — Merge Two Sorted Lists | Easy | Companies: Amazon, Apple, Meta, Microsoft, Google (Everywhere)

You are given the heads of two sorted linked lists `list1` and `list2`.
Merge them into one sorted linked list and return its head.
The merged list should be made by splicing together the nodes of the two input lists.

Examples:
  list1: 1 -> 2 -> 4,  list2: 1 -> 3 -> 4   ->  1 -> 1 -> 2 -> 3 -> 4 -> 4
  list1: [],           list2: []              ->  []
  list1: [],           list2: [0]             ->  [0]
  list1: 1 -> 3 -> 5,  list2: 2 -> 4 -> 6    ->  1 -> 2 -> 3 -> 4 -> 5 -> 6
  list1: 2,            list2: 1 -> 3          ->  1 -> 2 -> 3

Constraints:
  - Number of nodes in each list is in range [0, 50]
  - -100 <= Node.val <= 100
  - Both list1 and list2 are sorted in non-decreasing order
"""
