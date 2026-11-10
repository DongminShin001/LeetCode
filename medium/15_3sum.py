"""
#15 — 3Sum | Medium | Google, Meta, Amazon

Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i != j != k and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.

---

Example 1:
  Input:  nums = [-1, 0, 1, 2, -1, -4]
  Output: [[-1, -1, 2], [-1, 0, 1]]

  Sorted: [-4, -1, -1, 0, 1, 2]
  Fix -4: need pair summing to 4 → none found
  Fix -1 (index 1): need pair summing to 1 → (0,1) yes → [-1,0,1]
                                             → (-1,2) yes → [-1,-1,2]
  Fix -1 (index 2): duplicate of previous fixed value, skip
  Fix  0: need pair summing to 0 → (1,-1)? no remaining → none
  Result: [[-1,-1,2], [-1,0,1]]

Example 2:
  Input:  nums = [0, 1, 1]
  Output: []
  No three numbers sum to zero.

Example 3:
  Input:  nums = [0, 0, 0]
  Output: [[0, 0, 0]]

Example 4:
  Input:  nums = [-2, 0, 1, 1, 2]
  Sorted: [-2, 0, 1, 1, 2]
  Fix -2: need pair summing to 2 → (0,2) yes → [-2,0,2]
                                  → (1,1) yes → [-2,1,1]
  Fix  0: need pair summing to 0 → (1,-1)? not available → none
  Output: [[-2,0,2], [-2,1,1]]

Example 5:
  Input:  nums = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
  Output: [[-4,-2,6], [-4,0,4], [-4,1,3], [-4,2,2], [-2,-2,4], [-2,0,2]]
  (duplicates skipped by advancing past repeated values at each position)

---

Constraints:
  - 3 <= nums.length <= 3000
  - -10^5 <= nums[i] <= 10^5
"""
