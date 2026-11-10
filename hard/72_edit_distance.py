"""
72. Edit Distance
Difficulty: Hard
Companies: Google, Meta

Problem:
Given two strings word1 and word2, return the minimum number of operations
required to convert word1 into word2.
Allowed operations (each counts as 1):
  - Insert a character
  - Delete a character
  - Replace a character

Examples:

1. word1 = "horse", word2 = "ros"
   horse -> rorse (replace 'h' with 'r')
   rorse -> rose  (delete 'r')
   rose  -> ros   (delete 'e')
   Answer: 3

2. word1 = "intention", word2 = "execution"
   intention -> inention  (delete 't')
   inention  -> enention  (replace 'i' with 'e')
   enention  -> exention  (replace 'n' with 'x')
   exention  -> exection  (replace 'n' with 'c')
   exection  -> execution (insert 'u')
   Answer: 5

3. word1 = "", word2 = "a"
   Empty string to "a" requires 1 insertion.
   Answer: 1

4. word1 = "a", word2 = ""
   "a" to empty requires 1 deletion.
   Answer: 1

5. word1 = "abc", word2 = "abc"
   Identical strings, no operations needed.
   Answer: 0
"""
