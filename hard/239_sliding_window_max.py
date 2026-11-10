"""
239. Sliding Window Maximum
Difficulty: Hard
Companies: Google, Amazon

Problem:
Given an integer array nums and a sliding window of size k moving from the left
to right, return the max value in each window position. The window slides one
position at a time. There are n - k + 1 windows total.

Examples:

1. nums = [1,3,-1,-3,5,3,6,7], k = 3
   Window [1,3,-1]   -> max = 3
   Window [3,-1,-3]  -> max = 3
   Window [-1,-3,5]  -> max = 5
   Window [-3,5,3]   -> max = 5
   Window [5,3,6]    -> max = 6
   Window [3,6,7]    -> max = 7
   Answer: [3,3,5,5,6,7]

2. nums = [1], k = 1
   Single element, single window.
   Answer: [1]

3. nums = [1,-1], k = 1
   Window [1]  -> max = 1
   Window [-1] -> max = -1
   Answer: [1,-1]

4. nums = [9,11], k = 2
   Window [9,11] -> max = 11
   Answer: [11]

5. nums = [4,3,2,1,5], k = 3
   Window [4,3,2] -> max = 4
   Window [3,2,1] -> max = 3
   Window [2,1,5] -> max = 5
   Answer: [4,3,5]
"""
