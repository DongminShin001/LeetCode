"""
#684 — Redundant Connection | Medium | Google

You are given a graph that started as a tree with n nodes (labeled 1 to n) and one extra
edge was added. The graph is represented as an array edges where edges[i] = [a, b] indicates
an undirected edge between node a and node b.
Return the extra edge that can be removed to restore the tree.
If multiple answers exist, return the one that appears last in the input.

This is a Union-Find (Disjoint Set Union) problem.

---

Example 1:
  Input:  edges = [[1,2],[1,3],[2,3]]
  Output: [2,3]

  Process [1,2]: union 1 and 2 → different components, merge.
  Process [1,3]: union 1 and 3 → different components, merge.
  Process [2,3]: find(2) == find(3) → already in same component → redundant!
  Return [2,3].

Example 2:
  Input:  edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
  Output: [1,4]

  Process [1,2],[2,3],[3,4]: chain 1-2-3-4, all connected.
  Process [1,4]: find(1) == find(4) → cycle → redundant.
  Return [1,4].

Example 3:
  Input:  edges = [[1,2],[1,3],[2,4],[3,5],[4,5]]
  Output: [4,5]
  Adding [4,5] creates the first cycle.

Example 4:
  Input:  edges = [[3,4],[1,2],[2,4],[3,2],[1,5]]
  Output: [3,2]

Example 5:
  Input:  edges = [[1,2],[2,3],[1,3]]
  Process [1,2],[2,3]: 1-2-3 chain.
  Process [1,3]: already connected → redundant.
  Output: [1,3]

---

Constraints:
  - n == edges.length
  - 3 <= n <= 1000
  - edges[i].length == 2
  - 1 <= a, b <= n, a != b
  - No repeated edges.
  - The given graph is connected.
"""
