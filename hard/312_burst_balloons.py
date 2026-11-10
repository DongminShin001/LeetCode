"""
312. Burst Balloons
Difficulty: Hard
Companies: Google

Problem:
Given n balloons indexed 0 to n-1, each with a number on it. If you burst
balloon i, you gain nums[i-1] * nums[i] * nums[i+1] coins. After bursting,
adjacent balloons become neighbors. Return the maximum coins you can collect
by bursting all balloons.
Note: Treat nums[-1] = nums[n] = 1 (virtual boundary balloons).

Examples:

1. nums = [3,1,5,8]
   Augmented: [1,3,1,5,8,1]
   Optimal order: burst 1 -> 3*1*5=15, then burst 5 -> 3*5*8=120, then 3 -> 1*3*8=24, then 8 -> 1*8*1=8
   15+120+24+8 = 167
   Answer: 167

2. nums = [1,5]
   Augmented: [1,1,5,1]
   Burst 1 first: 1*1*5=5, then burst 5: 1*5*1=5. Total=10.
   Burst 5 first: 1*5*1=5, then burst 1: 1*1*1=1. Total=6.
   Best: 10
   Answer: 10

3. nums = [5]
   Only one balloon. 1*5*1 = 5.
   Answer: 5

4. nums = [1,2,3]
   Augmented: [1,1,2,3,1]
   Try all burst orders and pick max.
   Answer: 12

5. nums = [3,1,5]
   Augmented: [1,3,1,5,1]
   Key insight: think of which balloon is the LAST to burst in a range,
   not the first — this avoids dependency on burst order in DP.
   Answer: 35
"""
