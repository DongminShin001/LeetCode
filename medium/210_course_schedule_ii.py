"""
#210 — Course Schedule II | Medium | Google, Amazon

There are numCourses courses (labeled 0 to numCourses-1). Given prerequisites[i] = [a, b]
meaning course b must be taken before course a, return a valid ordering to take all courses.
If it is impossible (cycle exists), return an empty array.

This is a topological sort problem.

---

Example 1:
  Input:  numCourses = 2, prerequisites = [[1,0]]
  Output: [0, 1]
  Take 0 first, then 1.

Example 2:
  Input:  numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
  Graph: 0→1, 0→2, 1→3, 2→3
  Valid order: [0, 1, 2, 3] or [0, 2, 1, 3]
  Output: [0, 2, 1, 3]  (any valid topological order accepted)

Example 3:
  Input:  numCourses = 1, prerequisites = []
  Output: [0]

Example 4:
  Input:  numCourses = 3, prerequisites = [[1,0],[2,1]]
  Chain: 0 → 1 → 2
  Output: [0, 1, 2]

Example 5:
  Input:  numCourses = 2, prerequisites = [[0,1],[1,0]]
  Cycle detected → impossible.
  Output: []

---

Constraints:
  - 1 <= numCourses <= 2000
  - 0 <= prerequisites.length <= numCourses * (numCourses - 1)
  - prerequisites[i].length == 2
  - All (a, b) pairs are distinct.
"""
