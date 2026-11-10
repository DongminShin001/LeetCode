"""
295. Find Median from Data Stream
Difficulty: Hard
Companies: Google, Amazon, Meta

Problem:
Design a data structure that supports:
  - addNum(int num): Add an integer from the data stream.
  - findMedian() -> float: Return the median of all elements added so far.
If the total count is even, the median is the average of the two middle values.

Examples:

1. addNum(1), addNum(2), findMedian()
   Sorted so far: [1, 2]  (even count)
   Median = (1+2)/2 = 1.5
   Answer: 1.5

2. addNum(1), addNum(2), addNum(3), findMedian()
   Sorted so far: [1, 2, 3]  (odd count)
   Median = middle = 2
   Answer: 2.0

3. addNum(6), findMedian(), addNum(10), findMedian(), addNum(2), findMedian()
   After 6:    [6]      -> median = 6.0
   After 10:   [6,10]   -> median = (6+10)/2 = 8.0
   After 2:    [2,6,10] -> median = 6.0
   Answers: 6.0, 8.0, 6.0

4. addNum(-1), addNum(-2), addNum(-3), findMedian()
   Sorted: [-3,-2,-1]  (odd)
   Median = -2
   Answer: -2.0

5. addNum(5), addNum(5), addNum(5), findMedian()
   Sorted: [5,5,5]  (odd)
   Median = 5
   Answer: 5.0
"""
