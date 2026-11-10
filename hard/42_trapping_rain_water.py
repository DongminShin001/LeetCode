"""
42. Trapping Rain Water
Difficulty: Hard
Companies: Google, Amazon, Meta

Problem:
Given n non-negative integers representing an elevation map where each bar has
width 1, compute how much water it can trap after raining.

Examples:

1. height = [0,1,0,2,1,0,1,3,1,0,1,2]
   At index 5 (height 0): left max=2, right max=3 -> water = min(2,3)-0 = 2
   At index 9 (height 0): left max=3, right max=2 -> water = min(3,2)-0 = 2
   Sum all trapped water across each index.
   Answer: 6

2. height = [4,2,0,3,2,5]
   index 1: min(4,5)-2 = 2
   index 2: min(4,5)-0 = 4
   index 3: min(4,5)-3 = 1
   index 4: min(4,5)-2 = 2
   Answer: 9

3. height = [1,0,1]
   index 1: min(1,1)-0 = 1
   Answer: 1

4. height = [3,0,0,2,0,4]
   index 1: min(3,4)-0 = 3
   index 2: min(3,4)-0 = 3
   index 3: min(3,4)-2 = 1
   index 4: min(3,4)-0 = 3
   Answer: 10

5. height = [1,2,3,4,5]
   Strictly increasing — no water can be trapped anywhere.
   Each bar's left max is always less than the bar itself.
   Answer: 0
"""
