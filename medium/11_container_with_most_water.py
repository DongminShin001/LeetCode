"""
#11 — Container With Most Water | Medium | Google, Meta

Given an integer array height of length n representing vertical lines at positions 0..n-1,
find two lines that together with the x-axis form a container that holds the most water.
Return the maximum amount of water the container can store.
You may not slant the container.

Water held = min(height[left], height[right]) * (right - left)

---

Example 1:
  Input:  height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
  Output: 49

  Lines at index 1 (height 8) and index 8 (height 7):
  Water = min(8, 7) * (8 - 1) = 7 * 7 = 49

Example 2:
  Input:  height = [1, 1]
  Output: 1
  min(1,1) * (1-0) = 1

Example 3:
  Input:  height = [4, 3, 2, 1, 4]
  Candidates: (0,4) → min(4,4)*4 = 16  ← best
              (0,3) → min(4,1)*3 = 3
              (1,4) → min(3,4)*3 = 9
  Output: 16

Example 4:
  Input:  height = [1, 2, 1]
  (0,2): min(1,1)*2 = 2
  (0,1): min(1,2)*1 = 1
  (1,2): min(2,1)*1 = 1
  Output: 2

Example 5:
  Input:  height = [2, 3, 10, 5, 7, 8, 9]
  Best pair: index 2 (height 10) and index 6 (height 9)
  Water = min(10,9) * (6-2) = 9 * 4 = 36
  Output: 36

---

Constraints:
  - n == height.length
  - 2 <= n <= 10^5
  - 0 <= height[i] <= 10^4
"""
