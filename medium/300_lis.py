"""
#300 — Longest Increasing Subsequence | Medium | Google, Amazon

Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is derived by deleting some (or no) elements without changing the order of the rest.

---

Example 1:
  Input:  nums = [10, 9, 2, 5, 3, 7, 101, 18]
  Output: 4
  LIS: [2, 3, 7, 101] or [2, 5, 7, 101] or [2, 3, 7, 18]

Example 2:
  Input:  nums = [0, 1, 0, 3, 2, 3]
  Output: 4
  LIS: [0, 1, 2, 3] or [0, 1, 3] (length 3)... actually [0,1,2,3] = 4.

Example 3:
  Input:  nums = [7, 7, 7, 7, 7]
  All equal — strictly increasing requires strict inequality.
  Output: 1

Example 4:
  Input:  nums = [1, 3, 6, 7, 9, 4, 10, 5, 6]
  LIS: [1, 3, 6, 7, 9, 10] = length 6.
  Output: 6

Example 5:
  Input:  nums = [3, 10, 2, 1, 20]
  LIS options: [3,10,20] or [3,20] or [2,20] or [1,20]
  Best: [3, 10, 20] = length 3.
  Output: 3

---

Constraints:
  - 1 <= nums.length <= 2500
  - -10^4 <= nums[i] <= 10^4
  - Follow-up: can you do it in O(n log n)?
"""
