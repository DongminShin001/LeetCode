"""
759. Employee Free Time
Difficulty: Hard
Companies: Google

Problem:
Given a list of employees' schedules (each employee has a list of non-overlapping
intervals sorted by start time), return the list of finite intervals representing
common free time for all employees, also sorted. "Free time" means no employee is
working during that interval.

Examples:

1. schedule = [[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]]
   Employee 0 works: 1-3, 6-7
   Employee 1 works: 2-4
   Employee 2 works: 2-5, 9-12
   Merged working times: [1,5], [6,7], [9,12]
   Gaps: (5,6) and (7,9)
   Answer: [[5,6],[7,9]]

2. schedule = [[[1,2],[3,4]], [[2,3],[4,5]]]
   Employee 0: 1-2, 3-4
   Employee 1: 2-3, 4-5
   Merged: [1,5]  (all contiguous when combined)
   No gaps.
   Answer: []

3. schedule = [[[1,3]], [[3,6]], [[6,9]]]
   Merged: [1,9]  (all touch end-to-end)
   No gap — adjacent intervals touching at a point are not "free time".
   Answer: []

4. schedule = [[[1,2]], [[4,5]], [[7,8]]]
   Each employee works in separate windows.
   Gaps: (2,4), (5,7)
   Answer: [[2,4],[5,7]]

5. schedule = [[[1,5],[10,15]], [[3,8],[12,18]]]
   Employee 0: 1-5, 10-15
   Employee 1: 3-8, 12-18
   Merged: [1,8], [10,18]
   Gap: (8,10)
   Answer: [[8,10]]
"""
