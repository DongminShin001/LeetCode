"""
#647 — Palindromic Substrings | Medium | Amazon, Apple

Given a string s, return the number of palindromic substrings in it.
A substring is a contiguous sequence of characters within the string.
A string is palindromic if it reads the same forward and backward.

---

Example 1:
  Input:  s = "abc"
  Output: 3
  Palindromic substrings: "a", "b", "c"
  (no two-character palindromes since all chars differ)

Example 2:
  Input:  s = "aaa"
  Output: 6
  Substrings: "a"(x3), "aa"(x2), "aaa"(x1)
  All are palindromes: 3 + 2 + 1 = 6

Example 3:
  Input:  s = "aba"
  Output: 4
  "a" (i=0), "b" (i=1), "a" (i=2), "aba" (full string) = 4

Example 4:
  Input:  s = "abba"
  Palindromes: "a","b","b","a" (4 singles), "bb" (1), "abba" (1) = 6
  Output: 6

Example 5:
  Input:  s = "racecar"
  Singles: 7 ("r","a","c","e","c","a","r")
  Length 3: "cec" (centered at e), "aca", "racecar" is length 7...
  Expand from each center (odd and even):
    i=0 'r': "r"
    i=1 'a': "a", "rac"? no
    i=2 'c': "c", "ace"? no, "racecar"? r==r → yes
    i=3 'e': "e", "cec" yes, "aceca" yes, "racecar" yes
    etc.
  Output: 10

---

Constraints:
  - 1 <= s.length <= 1000
  - s consists of lowercase English letters.
"""
