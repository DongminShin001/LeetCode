"""
#56 — Merge Intervals | Medium | Google, Meta, Amazon

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping
intervals and return an array of the non-overlapping intervals that cover all the input intervals.

Two intervals overlap if one starts before or when the other ends.

---

Example 1:
  Input:  intervals = [[1,3],[2,6],[8,10],[15,18]]
  Output: [[1,6],[8,10],[15,18]]

  Sort by start: already sorted.
  [1,3] and [2,6] overlap (2 <= 3) → merge to [1,6]
  [1,6] and [8,10]: 8 > 6, no overlap → keep [8,10] separately
  [8,10] and [15,18]: 15 > 10, no overlap → keep
  Result: [[1,6],[8,10],[15,18]]

Example 2:
  Input:  intervals = [[1,4],[4,5]]
  Output: [[1,5]]
  Touching at 4 counts as overlapping → merged.

Example 3:
  Input:  intervals = [[1,4],[2,3]]
  Output: [[1,4]]
  [2,3] is completely inside [1,4].

Example 4:
  Input:  intervals = [[6,8],[1,9],[2,4],[4,7]]
  Sorted: [[1,9],[2,4],[4,7],[6,8]]
  All intervals are contained within [1,9].
  Output: [[1,9]]

Example 5:
  Input:  intervals = [[1,2],[3,4],[5,6]]
  No overlaps. Output: [[1,2],[3,4],[5,6]]

---

Constraints:
  - 1 <= intervals.length <= 10^4
  - intervals[i].length == 2
  - 0 <= start_i <= end_i <= 10^4
"""
