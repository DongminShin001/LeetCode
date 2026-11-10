"""
#78 — Subsets | Medium | Google, Meta, Amazon

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return in any order.
Total subsets = 2^n where n = len(nums).

---

Example 1:
  Input:  nums = [1, 2, 3]
  Output: [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

  At each element, decide to include or exclude:
  Start: [[]]
  Add 1: [[], [1]]
  Add 2: [[], [1], [2], [1,2]]
  Add 3: [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

Example 2:
  Input:  nums = [0]
  Output: [[], [0]]

Example 3:
  Input:  nums = [1, 2]
  Output: [[], [1], [2], [1,2]]

Example 4:
  Input:  nums = [1, 2, 3, 4]
  Total: 2^4 = 16 subsets.

Example 5:
  Input:  nums = [5, 3, 1] (order matters for backtracking traversal)
  Output: [[], [5], [3], [5,3], [1], [5,1], [3,1], [5,3,1]]
  (or any equivalent order)

---

Constraints:
  - 1 <= nums.length <= 10
  - -10 <= nums[i] <= 10
  - All elements of nums are unique.
"""
