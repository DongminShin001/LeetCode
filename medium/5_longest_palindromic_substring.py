"""
#5 — Longest Palindromic Substring | Medium | Amazon, Google

Given a string s, return the longest substring of s that is a palindrome.
A palindrome reads the same forward and backward.
If multiple answers exist with the same length, return any one.

---

Example 1:
  Input:  s = "babad"
  Output: "bab"  (or "aba" — both valid)

  Expand around each center:
    Center 'b' (i=0): "b" length 1
    Center 'a' (i=1): "a" / expand → "bab" length 3  ← best
    Center 'b' (i=2): "b" / expand → "aba" length 3
    Center 'a' (i=3): "a" / expand → "bad"? no. "a" length 1
    Center 'd' (i=4): "d" length 1

Example 2:
  Input:  s = "cbbd"
  Output: "bb"
  Even-length palindrome at positions (1,2): "bb" length 2.

Example 3:
  Input:  s = "a"
  Output: "a"

Example 4:
  Input:  s = "racecar"
  Entire string is a palindrome. Output: "racecar"

Example 5:
  Input:  s = "abacabad"
  Longest palindrome: "abacaba" (length 7).
  Output: "abacaba"

---

Constraints:
  - 1 <= s.length <= 1000
  - s consists of only digits and English letters.
"""
