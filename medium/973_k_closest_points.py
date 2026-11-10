"""
#973 — K Closest Points to Origin | Medium | Google, Amazon, Meta

Given an array of points where points[i] = [x_i, y_i] on the XY-plane and an integer k,
return the k closest points to the origin (0, 0).
Distance is Euclidean: sqrt(x^2 + y^2). You may compare x^2 + y^2 to avoid sqrt.
Return the answer in any order. The answer is guaranteed to be unique (no ties in distance).

---

Example 1:
  Input:  points = [[1,3],[-2,2]], k = 1
  Output: [[-2,2]]

  Distance^2 of [1,3]:  1 + 9  = 10
  Distance^2 of [-2,2]: 4 + 4  = 8  ← closer
  Return [-2,2].

Example 2:
  Input:  points = [[3,3],[5,-1],[-2,4]], k = 2
  Output: [[3,3],[-2,4]]

  Distances^2: [3,3]=18, [5,-1]=26, [-2,4]=20
  2 closest: [3,3](18) and [-2,4](20)

Example 3:
  Input:  points = [[0,1],[1,0]], k = 2
  Both have distance 1. Return both.
  Output: [[0,1],[1,0]]

Example 4:
  Input:  points = [[1,1],[2,2],[3,3]], k = 1
  Distances^2: 2, 8, 18. Closest: [1,1].
  Output: [[1,1]]

Example 5:
  Input:  points = [[-5,4],[1,2],[3,-1],[0,0]], k = 3
  Distances^2: 41, 5, 10, 0
  Sorted: [0,0](0), [1,2](5), [3,-1](10), [-5,4](41)
  Top 3: [[0,0],[1,2],[3,-1]]
  Output: [[0,0],[1,2],[3,-1]]

---

Constraints:
  - 1 <= k <= points.length <= 10^4
  - -10^4 <= x_i, y_i <= 10^4
"""
