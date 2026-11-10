"""
#46 — Permutations | Medium | Google, Meta, Amazon

Given an array nums of distinct integers, return all possible permutations in any order.

A permutation is an arrangement of all elements in a specific order.
Total permutations = n! where n = len(nums).

---

Example 1:
  Input:  nums = [1, 2, 3]
  Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

  Build by choosing each unused element at each position:
  Choose 1 → [1, _, _] → choose 2 → [1,2,3] and [1,3,2]
  Choose 2 → [2, _, _] → choose 1 → [2,1,3] and [2,3,1]
  Choose 3 → [3, _, _] → choose 1 → [3,1,2] and [3,2,1]

Example 2:
  Input:  nums = [0, 1]
  Output: [[0,1],[1,0]]

Example 3:
  Input:  nums = [1]
  Output: [[1]]

Example 4:
  Input:  nums = [1, 2, 3, 4]
  Output: 24 permutations total (4! = 24)

Example 5:
  Input:  nums = [-1, 2, 0]
  Output: [[-1,2,0],[-1,0,2],[2,-1,0],[2,0,-1],[0,-1,2],[0,2,-1]]

---

Constraints:
  - 1 <= nums.length <= 6
  - -10 <= nums[i] <= 10
  - All integers in nums are unique.
"""
