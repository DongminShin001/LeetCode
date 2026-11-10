"""
642. Design Search Autocomplete System
Difficulty: Hard
Companies: Google

Problem:
Design a search autocomplete system. Users type a query character by character.
After each character, return the top 3 historical sentences with the highest
frequency that have the typed prefix. Ties broken by ASCII order.
  - Input(c): If c != '#', add character to current input and return top 3 matches.
              If c == '#', save the current sentence with incremented frequency, reset input, return [].

Examples:

1. sentences = ["i love you","island","iroman","i love leetcode"], times = [5,3,2,2]
   input('i')   -> prefix "i": matches all 4. Top 3 by freq: ["i love you"(5), "island"(3), "i love leetcode"(2)]
                   (tie between "iroman" and "i love leetcode" -> ASCII order: "i love leetcode" < "iroman")
   input(' ')   -> prefix "i ": "i love you"(5), "i love leetcode"(2)
                   -> ["i love you","i love leetcode"]
   input('a')   -> prefix "i a": no matches -> []
   input('#')   -> save "i a" with freq 1, reset -> []

2. (continuing above)
   input('i')   -> prefix "i": now "i a" has freq 1 too.
                   Top 3: ["i love you"(5), "island"(3), "i love leetcode"(2)]
                   (i a has freq 1, doesn't make top 3)

3. input('z')   -> prefix "z": no historical sentence starts with "z" -> []
   input('#')   -> saves "z", freq=1, resets -> []
   input('z')   -> prefix "z": ["z"]  (now "z" is in history with freq 1)

4. sentences = ["abc","abbc","a"], times = [3,3,3]
   input('a')   -> all 3 match prefix "a". Tie on freq=3, sort by ASCII: ["a","abc","abbc"]

5. input('a'), input('b'), input('c'), input('#')
   "abc" freq incremented. Next input('a'), input('b') ->
   prefix "ab": shows "abc" at top (higher freq now).
"""
