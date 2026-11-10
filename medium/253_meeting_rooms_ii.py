"""
#253 — Meeting Rooms II | Medium | Google, Meta, Amazon

Given an array of meeting time intervals intervals[i] = [start_i, end_i],
return the minimum number of conference rooms required to hold all meetings simultaneously.

A room is free once a meeting ends (end time is exclusive / just freed at that moment).

---

Example 1:
  Input:  intervals = [[0,30],[5,10],[15,20]]
  Output: 2

  Timeline:
    t=0:  meeting [0,30] starts → 1 room in use
    t=5:  meeting [5,10] starts, [0,30] still going → 2 rooms in use  ← peak
    t=10: [5,10] ends → 1 room in use
    t=15: [15,20] starts → 2 rooms in use
    t=20: [15,20] ends → 1 room
    t=30: [0,30] ends → 0 rooms
  Max concurrent = 2

Example 2:
  Input:  intervals = [[7,10],[2,4]]
  Output: 1
  [2,4] ends before [7,10] starts → one room is enough.

Example 3:
  Input:  intervals = [[1,5],[2,6],[3,7]]
  All three overlap at t=3,4,5.
  Output: 3

Example 4:
  Input:  intervals = [[1,4],[2,5],[7,9]]
  At t=2: [1,4] and [2,5] overlap → 2 rooms.
  [7,9] starts after both end → reuse a room.
  Output: 2

Example 5:
  Input:  intervals = [[9,10],[4,9],[4,17]]
  Sorted starts: 4, 4, 9
  t=4: 2 meetings start → 2 rooms
  t=9: [4,9] ends, [9,10] starts → still 2 rooms
  t=10: [9,10] ends → 1 room
  t=17: [4,17] ends → 0 rooms
  Output: 2

---

Constraints:
  - 1 <= intervals.length <= 10^4
  - 0 <= start_i < end_i <= 10^6
"""
