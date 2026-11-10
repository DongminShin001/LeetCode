"""
#57 — Insert Interval | Medium | Google

You are given an array of non-overlapping intervals sorted by start time, and a single
new interval to insert. Insert it into the list so the result remains sorted and
non-overlapping (merge as necessary). Return the updated list.

---

Example 1:
  Input:  intervals = [[1,3],[6,9]], newInterval = [2,5]
  Output: [[1,5],[6,9]]

  [1,3] and [2,5] overlap (2 <= 3) → merge to [1,5]
  [1,5] and [6,9]: 6 > 5 → no overlap
  Result: [[1,5],[6,9]]

Example 2:
  Input:  intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
  Output: [[1,2],[3,10],[12,16]]

  [1,2]: ends before 4 → keep as is
  [3,5]: overlaps [4,8] (4 <= 5) → start merging, current = [3,8]
  [6,7]: overlaps [3,8] → extend, current = [3,8]
  [8,10]: overlaps (8 <= 8) → extend, current = [3,10]
  [12,16]: 12 > 10 → no overlap, emit [3,10], keep [12,16]
  Result: [[1,2],[3,10],[12,16]]

Example 3:
  Input:  intervals = [], newInterval = [5,7]
  Output: [[5,7]]

Example 4:
  Input:  intervals = [[1,5]], newInterval = [2,3]
  newInterval is fully inside [1,5] → Output: [[1,5]]

Example 5:
  Input:  intervals = [[1,5]], newInterval = [6,8]
  No overlap. Output: [[1,5],[6,8]]

---

Constraints:
  - 0 <= intervals.length <= 10^4
  - intervals[i].length == 2
  - 0 <= start_i <= end_i <= 10^5
  - intervals is sorted by start_i in ascending order
  - newInterval.length == 2
"""
