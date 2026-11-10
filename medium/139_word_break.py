"""
#139 — Word Break | Medium | Google, Meta, Amazon

Given a string s and a dictionary of strings wordDict, return true if s can be segmented
into a space-separated sequence of one or more dictionary words.
Words in the dictionary may be reused multiple times.

---

Example 1:
  Input:  s = "leetcode", wordDict = ["leet","code"]
  Output: True
  "leet" + "code" = "leetcode"

Example 2:
  Input:  s = "applepenapple", wordDict = ["apple","pen"]
  Output: True
  "apple" + "pen" + "apple" = "applepenapple"

Example 3:
  Input:  s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
  Output: False
  Possible splits:
    "cat" + "sandog" → "sandog" can't be formed
    "cats" + "andog" → "andog" can't be formed
  No valid segmentation.

Example 4:
  Input:  s = "aaaaaaa", wordDict = ["aaaa","aaa"]
  Output: True
  "aaa" + "aaaa" = "aaaaaaa"
  (also "aaaa" + "aaa")

Example 5:
  Input:  s = "goalspecial", wordDict = ["go","goal","goals","special"]
  Output: True
  "goal" + "special" = "goalspecial"
  (note: "go" + "als" doesn't work since "als" not in dict)

---

Constraints:
  - 1 <= s.length <= 300
  - 1 <= wordDict.length <= 1000
  - 1 <= wordDict[i].length <= 20
  - s and wordDict[i] consist of lowercase English letters only.
  - All strings in wordDict are unique.
"""
