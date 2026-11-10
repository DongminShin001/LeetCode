"""
10. Regular Expression Matching
Difficulty: Hard
Companies: Google

Problem:
Given an input string s and a pattern p, implement regular expression matching
with support for '.' and '*'.
  '.'  matches any single character.
  '*'  matches zero or more of the preceding element.
The matching must cover the entire input string (not partial).

Examples:

1. s = "aa", p = "a"
   Pattern "a" only matches one 'a', but s has two.
   Answer: False

2. s = "aa", p = "a*"
   "a*" means zero or more 'a'. Matches "aa".
   Answer: True

3. s = "ab", p = ".*"
   ".*" means zero or more of any character. Matches any string.
   Answer: True

4. s = "aab", p = "c*a*b"
   "c*" -> zero c's (skip), "a*" -> two a's, "b" -> one b.
   Matches "aab".
   Answer: True

5. s = "mississippi", p = "mis*is*p*."
   "m"->m, "i"->i, "s*"->ss, "i"->i, "s*"->ss, "p*"->zero p, "."->p?
   Stuck — 'p*' eats one 'p', then '.' must match 'p', but we also have 'i' remaining.
   Careful tracing needed; DP is typically used.
   Answer: False
"""
