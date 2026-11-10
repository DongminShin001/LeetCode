"""
269. Alien Dictionary
Difficulty: Hard
Companies: Google, Meta, Uber

Problem:
You are given a list of words sorted lexicographically according to the rules
of an unknown alien language. Derive the order of the alphabet letters from
the word list. Return any valid ordering. If the order is invalid (cycle), return "".
If multiple valid orderings exist, return any one.

Examples:

1. words = ["wrt","wrf","er","ett","rftt"]
   Compare adjacent words:
   "wrt" vs "wrf": t < f
   "wrf" vs "er":  w < e
   "er"  vs "ett": r < t
   "ett" vs "rftt": e < r
   Topological order from edges {t->f, w->e, r->t, e->r}:
   w -> e -> r -> t -> f
   Answer: "wertf"

2. words = ["z","x"]
   "z" vs "x": z < x
   Answer: "zx"

3. words = ["z","x","z"]
   "x" vs "z" gives x < z, but earlier "z" vs "x" gives z < x. Cycle!
   Answer: ""

4. words = ["abc","ab"]
   "abc" comes before "ab" but "abc" is a prefix of... wait, "ab" is a prefix of "abc".
   A longer word coming before its prefix is invalid in any ordering.
   Answer: ""

5. words = ["ac","ab","b"]
   "ac" vs "ab": c < b
   "ab" vs "b":  a < b
   Edges: c->b, a->b
   Both c and a come before b. Valid order: a, c, b or c, a, b.
   Answer: "acb" (or "cab")
"""
