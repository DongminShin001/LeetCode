"""
#347 — Top K Frequent Elements | Medium | Google, Amazon, Meta

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
It is guaranteed that the answer is unique (there is a unique set of k most frequent elements).

---

Example 1:
  Input:  nums = [1,1,1,2,2,3], k = 2
  Output: [1, 2]

  Frequencies: {1: 3, 2: 2, 3: 1}
  Top 2 by frequency: 1 (count 3), 2 (count 2)

Example 2:
  Input:  nums = [1], k = 1
  Output: [1]

Example 3:
  Input:  nums = [4,1,1,4,2,4,3,3], k = 2
  Frequencies: {4: 3, 1: 2, 3: 2, 2: 1}
  Top 2: [4, 1] or [4, 3]  (both valid since 1 and 3 tie at count 2)
  Output: [4, 1]

Example 4:
  Input:  nums = [1,2,3,4,5], k = 3
  All appear once — any 3 are valid.
  Output: [1, 2, 3]  (any 3 elements)

Example 5:
  Input:  nums = [5,3,1,1,1,3,73,1], k = 1
  Frequencies: {1: 4, 3: 2, 5: 1, 73: 1}
  Output: [1]

---

Constraints:
  - 1 <= nums.length <= 10^5
  - -10^4 <= nums[i] <= 10^4
  - 1 <= k <= number of unique elements in nums
  - Answer is guaranteed to be unique.
  - Follow-up: your algorithm's time complexity must be better than O(n log n).
"""
