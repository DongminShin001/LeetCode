"""
212. Word Search II
Difficulty: Hard
Companies: Google, Amazon

Problem:
Given an m x n board of characters and a list of words, return all words that
can be found in the board. A word is formed by sequentially adjacent cells
(horizontally or vertically), and each cell may not be reused within a single word.

Examples:

1. board = [["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]]
   words = ["oath","pea","eat","rain"]
   Trace "eat":  board[1][3]='e' -> board[1][2]='a' -> board[0][2]='a'? no, need 't'.
         board[1][3]='e' -> board[0][3]='a'? no. board[1][1]='t'... try e(1,3)->a(1,2)->t? 'a' != 't'.
         e(1,3)->a(1,2) no 't' neighbor... e(0,0)? no. Eventually found via e->a->t path.
   Trace "oath": o(0,0)->a(0,1)->t(1,1)->h(2,1) — valid path.
   Answer: ["eat","oath"]

2. board = [["a","b"],["c","d"]]
   words = ["abdc","abcd","cdba"]
   "abdc": a(0,0)->b(0,1)->d(1,1)->c(1,0) — valid path.
   "abcd": a(0,0)->b(0,1)->c? 'c' not adjacent to b. Invalid.
   "cdba": c(1,0)->d(1,1)->b(0,1)->a(0,0) — valid path.
   Answer: ["abdc","cdba"]

3. board = [["a"]]
   words = ["a"]
   Single cell matches "a" directly.
   Answer: ["a"]

4. board = [["a","a"]]
   words = ["aaa"]
   Only 2 cells, can't form 3-char word without reuse.
   Answer: []

5. board = [["o","a","b","n"],
            ["o","t","a","e"],
            ["a","h","k","r"],
            ["a","f","l","v"]]
   words = ["oa","oat","oath","oath","ab"]
   "oa": o(0,0)->a(0,1) or o(1,0)->a(1,2)?  o(0,0)->a(0,1) valid.
   "oat": o(0,0)->a(0,1)->t(1,1) valid.
   "oath": o(0,0)->a(0,1)->t(1,1)->h(2,1) valid.
   "ab": a(0,1)->b(0,2) valid.
   Answer: ["oa","oat","oath","ab"]
"""
