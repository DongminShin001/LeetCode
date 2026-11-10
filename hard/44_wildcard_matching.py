"""
44. Wildcard Matching
Difficulty: Hard
Companies: Google

Problem:
Given an input string s and a pattern p, implement wildcard pattern matching.
  '?' matches any single character.
  '*' matches any sequence of characters (including empty sequence).
The matching must cover the entire input string.

Examples:

1. s = "aa", p = "a"
   Pattern "a" only matches one character. s has two.
   Answer: False

2. s = "aa", p = "*"
   '*' matches any sequence, including "aa".
   Answer: True

3. s = "cb", p = "?a"
   '?' matches 'c', then 'a' must match 'b'. 'a' != 'b'.
   Answer: False

4. s = "adceb", p = "*a*b"
   '*' matches "" , 'a' matches 'a', '*' matches "dce", 'b' matches 'b'.
   Answer: True

5. s = "acdcb", p = "a*c?b"
   'a'->a, '*' matches "" or "cd", 'c'->c, '?'->?, 'b'->b.
   Try: a + * matches "d" + c matches 'c' + ? matches '?' + b matches 'b'.
   a + "*"="d" + c + "?"=last before b...
   "acdcb": a,*->""->c->d? doesn't work. a,*->cd,c->c,?->b... no. No valid split.
   Answer: False
"""
