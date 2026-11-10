"""
#39 — Combination Sum | Medium | Google, Meta, Amazon

Given an array of distinct integers candidates and a target integer target, return all
unique combinations of candidates that sum to target.
You may use the same number from candidates an unlimited number of times.
The same combination (regardless of order) must not appear twice.

---

Example 1:
  Input:  candidates = [2, 3, 6, 7], target = 7
  Output: [[2,2,3],[7]]

  Backtrack:
  Start with 2: 2 → 2,2 → 2,2,2 (sum=6) → 2,2,2,2 (too big) → backtrack
                               → 2,2,3 (sum=7) ✓
               → 2,2,6 (too big) → ...
  Start with 3: 3 → 3,3 (6) → 3,3,3 (too big) → 3,3,6 (too big)
  ...
  Start with 7: 7 ✓

Example 2:
  Input:  candidates = [2, 3, 5], target = 8
  Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
  Input:  candidates = [2], target = 1
  Smallest candidate is 2 > 1. Output: []

Example 4:
  Input:  candidates = [1], target = 4
  Output: [[1,1,1,1]]

Example 5:
  Input:  candidates = [3, 5, 8], target = 11
  3+3+5=11, 3+8=11
  Output: [[3,3,5],[3,8]]

---

Constraints:
  - 1 <= candidates.length <= 30
  - 2 <= candidates[i] <= 40
  - All elements of candidates are distinct.
  - 1 <= target <= 40
"""
