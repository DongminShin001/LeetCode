"""
76. Minimum Window Substring
Difficulty: Hard
Companies: Google, Meta, Amazon

Problem:
Given two strings s and t, return the minimum window substring of s such that
every character in t (including duplicates) is included in the window.
If no such window exists, return "". The answer is guaranteed to be unique.

Examples:

1. s = "ADOBECODEBANC", t = "ABC"
   Scan right until window contains A,B,C: "ADOBEC" (index 0..5)
   Try shrinking left: remove 'A' -> "DOBEC" missing A. Stop.
   Continue right, found 'A' at index 10: "DOBECODEBA" -> shrink...
   Best window found: "BANC" (index 9..12)
   Answer: "BANC"

2. s = "a", t = "a"
   Window "a" contains 'a'. Already minimal.
   Answer: "a"

3. s = "a", t = "aa"
   Only one 'a' in s, but t needs two. Impossible.
   Answer: ""

4. s = "ABCDE", t = "ACE"
   Full scan: "ABCDE" contains A,C,E.
   Shrink: remove 'A' -> "BCDE" missing A. Can't shrink more from left.
   Try window starting further... no smaller window found.
   Answer: "ABCDE"

5. s = "cabwefgewcwaefgcf", t = "cae"
   Windows containing c,a,e:
   "cabwefgewcwaefgcf" -> scan and shrink.
   Minimum window found: "cwae" or "aefgc"? Trace carefully.
   Answer: "cwae"
"""
