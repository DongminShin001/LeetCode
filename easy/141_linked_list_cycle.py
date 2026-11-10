"""
#141 — Linked List Cycle | Easy | Companies: Amazon, Apple, Meta, Microsoft, Google (Everywhere)

Given the head of a linked list, determine if the list contains a cycle.
A cycle exists if some node can be reached again by continuously following the `next` pointer.
Internally, `pos` denotes the index (0-based) of the node that the tail connects back to.
`pos` is not passed as a parameter — it is only for problem illustration.
Return true if there is a cycle, false otherwise.

Examples:
  3 -> 2 -> 0 -> -4 (tail connects to index 1)   ->  true
  1 -> 2            (tail connects to index 0)    ->  true
  [1]               (no cycle, pos = -1)           ->  false
  1 -> 2 -> 3 -> 4  (no cycle, pos = -1)           ->  false
  1 -> 2 -> 3 -> 4 -> 5 (tail connects to index 2) ->  true

Constraints:
  - Number of nodes is in range [0, 10^4]
  - -10^5 <= Node.val <= 10^5
  - pos is -1 or a valid index in the linked list

Follow-up: Can you solve it using O(1) memory?
"""
