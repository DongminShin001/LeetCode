"""
410. Split Array Largest Sum
Difficulty: Hard
Companies: Google

Problem:
Given an integer array nums and an integer k, split nums into k non-empty
subarrays such that the largest sum among these subarrays is minimized.
Return that minimized largest sum.

Examples:

1. nums = [7,2,5,10,8], k = 2
   Possible splits:
   [7] [2,5,10,8] -> max(7, 25) = 25
   [7,2] [5,10,8] -> max(9, 23) = 23
   [7,2,5] [10,8] -> max(14, 18) = 18  <- best
   [7,2,5,10] [8] -> max(24, 8) = 24
   Answer: 18

2. nums = [1,2,3,4,5], k = 2
   [1,2,3] [4,5] -> max(6,9) = 9
   [1,2,3,4] [5] -> max(10,5) = 10
   [1,2] [3,4,5] -> max(3,12) = 12
   Answer: 9

3. nums = [1,4,4], k = 3
   Each element in its own subarray: max(1,4,4) = 4.
   Answer: 4

4. nums = [1,2,3,4,5], k = 1
   Only one subarray = all elements. Sum = 15.
   Answer: 15

5. nums = [2,3,1,2,4,3], k = 5
   Try splits that minimize the largest chunk.
   Answer: 4
"""
