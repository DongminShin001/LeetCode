"""
#743 — Network Delay Time | Medium | Google, Amazon

You are given a network of n nodes labeled 1 to n, and a list of travel times as
directed edges times[i] = [u, v, w] where u is source, v is target, w is travel time.
A signal is sent from node k. Return the minimum time for all n nodes to receive the signal.
If it is impossible for all nodes to receive the signal, return -1.

This is a single-source shortest path problem (Dijkstra's algorithm).

---

Example 1:
  Input:  times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
  Output: 2

  From node 2:
    → node 1: cost 1
    → node 3: cost 1
    → node 4 (via 3): cost 1+1 = 2
  All nodes reached. Max time = 2.

Example 2:
  Input:  times = [[1,2,1]], n = 2, k = 1
  Output: 1
  Node 2 reached in 1 unit.

Example 3:
  Input:  times = [[1,2,1]], n = 2, k = 2
  Output: -1
  Node 2 can't reach node 1 (no edge from 2 to 1).

Example 4:
  Input:  times = [[1,2,1],[2,3,2],[1,3,4]], n = 3, k = 1
  Shortest to 2: 1 (direct)
  Shortest to 3: min(4, 1+2) = 3 (via 2)
  Max = 3. Output: 3

Example 5:
  Input:  times = [[1,2,1],[2,3,1],[3,2,1]], n = 3, k = 1
  Shortest to 2: 1
  Shortest to 3: 2
  All reachable. Output: 2

---

Constraints:
  - 1 <= k <= n <= 100
  - 1 <= times.length <= 6000
  - times[i].length == 3
  - 1 <= u, v <= n, u != v
  - 0 <= w <= 100
  - All (u, v) pairs are unique.
"""
