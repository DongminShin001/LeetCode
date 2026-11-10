"""
#49 — Group Anagrams | Medium | Google, Amazon, Meta

Given an array of strings strs, group the anagrams together and return them in any order.
An anagram is a word formed by rearranging the letters of another word using all original letters exactly once.

---

Example 1:
  Input:  strs = ["eat","tea","tan","ate","nat","bat"]
  Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

  sorted("eat") = "aet", sorted("tea") = "aet", sorted("ate") = "aet" → same group
  sorted("tan") = "ant", sorted("nat") = "ant" → same group
  sorted("bat") = "abt" → its own group

Example 2:
  Input:  strs = [""]
  Output: [[""]]

Example 3:
  Input:  strs = ["a"]
  Output: [["a"]]

Example 4:
  Input:  strs = ["abc","bca","cab","xyz","zyx"]
  Groups: ["abc","bca","cab"] (all sort to "abc") and ["xyz","zyx"] (sort to "xyz")
  Output: [["abc","bca","cab"],["xyz","zyx"]]

Example 5:
  Input:  strs = ["", "b", "", "a"]
  Groups: ["",""] (empty strings) and ["b"] and ["a"]
  Output: [["",""],["b"],["a"]]

---

Constraints:
  - 1 <= strs.length <= 10^4
  - 0 <= strs[i].length <= 100
  - strs[i] consists of lowercase English letters.
"""
