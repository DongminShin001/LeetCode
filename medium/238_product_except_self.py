"""
#238 — Product of Array Except Self | Medium | Google, Meta, Amazon

Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all elements of nums except nums[i].
You must solve it in O(n) time without using the division operation.

---

Example 1:
  Input:  nums = [1, 2, 3, 4]
  Output: [24, 12, 8, 6]

  For index 0: 2*3*4 = 24
  For index 1: 1*3*4 = 12
  For index 2: 1*2*4 = 8
  For index 3: 1*2*3 = 6

  Prefix products (left of i): [1, 1, 2, 6]
  Suffix products (right of i): [24, 12, 4, 1]
  answer[i] = prefix[i] * suffix[i] = [24, 12, 8, 6]

Example 2:
  Input:  nums = [-1, 1, 0, -3, 3]
  Output: [0, 0, 9, 0, 0]

  Index 2 is 0; all other positions include that 0 in their product.
  Index 2 itself: (-1)*1*(-3)*3 = 9

Example 3:
  Input:  nums = [2, 3, 4]
  prefix: [1, 2, 6]
  suffix: [12, 4, 1]
  answer: [12, 8, 6]
  Output: [12, 8, 6]

Example 4:
  Input:  nums = [0, 0]
  Output: [0, 0]
  Each side has a zero, so both products are 0.

Example 5:
  Input:  nums = [5]
  Output: [1]
  Product of empty set = 1.

---

Constraints:
  - 2 <= nums.length <= 10^5
  - -30 <= nums[i] <= 30
  - The product of any prefix or suffix fits in a 32-bit integer.
  - Follow-up: solve with O(1) extra space (output array doesn't count).
"""
