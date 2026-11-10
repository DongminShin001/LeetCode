"""
#207 — Course Schedule | Medium | Google, Meta, Amazon

There are numCourses courses (labeled 0 to numCourses-1). You are given an array
prerequisites where prerequisites[i] = [a, b] means you must take course b before course a.
Return true if you can finish all courses, false if there is a cycle.

This is equivalent to: does the directed graph of prerequisites contain a cycle?

---

Example 1:
  Input:  numCourses = 2, prerequisites = [[1,0]]
  Output: True
  Take course 0 first, then course 1. No cycle.

Example 2:
  Input:  numCourses = 2, prerequisites = [[1,0],[0,1]]
  Output: False
  Course 1 requires 0, and course 0 requires 1 → cycle: 0 → 1 → 0

Example 3:
  Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  Graph: 0→1, 0→2, 1→3, 2→3
  No cycle — topological order: 0, 1, 2, 3 (or 0, 2, 1, 3)
  Output: True

Example 4:
  Input:  numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]
  Cycle: 0 → 1 → 2 → 0
  Output: False

Example 5:
  Input:  numCourses = 1, prerequisites = []
  No prerequisites, just take course 0.
  Output: True

---

Constraints:
  - 1 <= numCourses <= 2000
  - 0 <= prerequisites.length <= 5000
  - prerequisites[i].length == 2
  - 0 <= a, b < numCourses
  - All (a, b) pairs are distinct.
"""
