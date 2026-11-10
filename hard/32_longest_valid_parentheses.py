"""
32. Longest Valid Parentheses
Difficulty: Hard
Companies: Google, Meta

Problem:
Given a string containing only '(' and ')', return the length of the longest
valid (well-formed) parentheses substring.

Examples:

1. s = "(()"
   Valid substrings: "()" at index 1-2, length 2.
   The leading '(' at index 0 has no matching ')'.
   Answer: 2

2. s = ")()())"
   Valid substrings: "()" at 1-2, "()()" at 1-4 — length 4.
   The ')' at index 0 and 5 break the sequence.
   Answer: 4

3. s = ""
   Empty string, no valid parentheses.
   Answer: 0

4. s = "()(()"
   "()" at 0-1, length 2.
   "((" at 2-3 invalid. "()" at 3-4, length 2.
   No way to combine into longer valid sequence.
   Answer: 2

5. s = "()(())"
   "()" at 0-1, length 2.
   "(())" at 2-5, length 4.
   Combined: "()(())" at 0-5, all valid, length 6.
   Answer: 6
"""
