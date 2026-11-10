"""
127. Word Ladder
Difficulty: Hard
Companies: Google, Amazon

Problem:
Given two words, beginWord and endWord, and a word list (dictionary), find the
length of the shortest transformation sequence from beginWord to endWord such that:
  - Only one letter can be changed at a time.
  - Each transformed word must exist in the word list.
Return the number of words in the shortest path, or 0 if no such path exists.

Examples:

1. beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
   hit -> hot -> dot -> dog -> cog
   Answer: 5  (5 words in the chain)

2. beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
   "cog" not in wordList — no valid path.
   Answer: 0

3. beginWord = "a", endWord = "c", wordList = ["a","b","c"]
   a -> c?  differ by 1 letter, "c" in list.
   a -> c directly (1 change).
   Answer: 2

4. beginWord = "hot", endWord = "dog", wordList = ["hot","dog"]
   hot -> dog: h!=d, o==o, t!=g — 2 letters differ, can't go directly.
   No intermediate word available.
   Answer: 0

5. beginWord = "game", endWord = "thee", wordList = ["fame","fate","late","lane","line","mine","mite","site","sire","fire","fore","more","gore","gone","tone","tune","dune","dude","duke","like","bike","bite","mite","thee","tree","free","flee","flat","fiat","feat","heat","heap","reap","read","bead","dead","dean","bean","lean","lead","load","toad","told","cold","cord","core","bore","lore","lure","lute","lore","more","mare","dare","date","late","fate","face","lace","race","rice","dice","dine","mine","wine","wire","hire","here","hare","bare","base","case","cave","cave","have","gave","give","live","like","bike","bake","lake","fake","face","lace","race","rice","nice","mice","mile","mile","tile","time","lime","line","vine","vane","cane","came","game"]
   Long chain exists.
   Answer: some integer > 0
"""
