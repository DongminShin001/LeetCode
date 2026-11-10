"""
4. Median of Two Sorted Arrays
Difficulty: Hard
Companies: Google, Amazon

Problem:
Given two sorted arrays nums1 and nums2 of sizes m and n, return the median
of the two sorted arrays combined. The overall runtime complexity must be
O(log(m + n)).

Examples:

1. nums1 = [1,3], nums2 = [2]
   Merged: [1,2,3]  (length 3, odd)
   Median = middle element = 2
   Answer: 2.0

2. nums1 = [1,2], nums2 = [3,4]
   Merged: [1,2,3,4]  (length 4, even)
   Median = (2+3)/2 = 2.5
   Answer: 2.5

3. nums1 = [0,0], nums2 = [0,0]
   Merged: [0,0,0,0]
   Median = (0+0)/2 = 0.0
   Answer: 0.0

4. nums1 = [], nums2 = [1]
   Merged: [1]
   Median = 1
   Answer: 1.0

5. nums1 = [2], nums2 = []
   Merged: [2]
   Median = 2
   Answer: 2.0
"""
