"""
#1 — Two Sum | Easy | Companies: Google, Amazon, Apple, Meta, Microsoft (Everywhere)

Given an array of integers `nums` and an integer `target`, return the indices
of the two numbers that add up to `target`. Each input has exactly one solution,
and you may not use the same element twice. Return the answer in any order.

Examples:
  nums = [2, 7, 11, 15], target = 9       -> [0, 1]       (2 + 7 = 9)
  nums = [3, 2, 4],       target = 6       -> [1, 2]       (2 + 4 = 6)
  nums = [3, 3],          target = 6       -> [0, 1]       (3 + 3 = 6)
  nums = [1, 5, 3, 2],    target = 4       -> [2, 3]       (3 + 2 = 5... wait: 1+3=4 -> [0,2])
  nums = [-1, -2, -3, -4], target = -6     -> [1, 3]       (-2 + -4 = -6)

Constraints:
  - 2 <= nums.length <= 10^4
  - -10^9 <= nums[i] <= 10^9
  - -10^9 <= target <= 10^9
  - Exactly one valid answer exists
"""
