"""
LeetCode #146 - LRU Cache  |  Hard  |  Google, Meta, Amazon, Microsoft

Design a data structure that follows Least Recently Used (LRU) eviction.

Implement LRUCache(capacity):
  get(key)        -> return value if key exists, else -1
                     accessing a key marks it as most recently used
  put(key, value) -> insert or update key
                     if over capacity, evict the least recently used key

Both get and put must run in O(1) average time.

------------------------------------------------------------
Example 1
  cache = LRUCache(2)
  put(1,1) put(2,2) get(1)->1  put(3,3) get(2)->-1  put(4,4) get(1)->-1  get(3)->3  get(4)->4

Example 2 - updating existing key
  cache = LRUCache(2)
  put(1,10) put(2,20) put(1,99) put(3,30) get(1)->99  get(2)->-1  get(3)->30

Example 3 - capacity 1
  cache = LRUCache(1)
  put(1,1) put(2,2) get(1)->-1  get(2)->2

Example 4 - get refreshes recency
  cache = LRUCache(2)
  put(2,1) put(1,1) put(2,3) put(4,1) get(1)->-1  get(2)->3

Example 5 - stress
  cache = LRUCache(3)
  put(1,1) put(2,2) put(3,3) get(1)->1  put(4,4) get(2)->-1  get(3)->3  put(5,5) get(1)->-1  get(4)->4
------------------------------------------------------------
"""

"""
1. dobuly linked list 
prev node 
next node 

2. hash map 
key = key of cache
value = node => memroy and it s unique 


"""
from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRU:
    def __init__(self, size):
        # doubly linked list
        self.hash = defaultdict() #i do not need to check key eixit 
        self.max = size
        self.size = 0

    def put(self, node):
        

    def get(self, node):

        