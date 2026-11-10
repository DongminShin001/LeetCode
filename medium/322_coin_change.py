"""
#322 — Coin Change | Medium | Google, Amazon, Meta

You are given an integer array coins representing coin denominations and an integer amount.
Return the fewest number of coins needed to make up that amount.
If the amount cannot be made up by any combination, return -1.
You may use each coin denomination an unlimited number of times.

---

Example 1:
  Input:  coins = [1, 2, 5], amount = 11
  Output: 3  (5 + 5 + 1)

  dp[0] = 0
  dp[1] = 1 (1)
  dp[2] = 1 (2)
  dp[3] = 2 (2+1)
  dp[4] = 2 (2+2)
  dp[5] = 1 (5)
  dp[6] = 2 (5+1)
  dp[7] = 2 (5+2)
  dp[11] = 3 (5+5+1)

Example 2:
  Input:  coins = [2], amount = 3
  Output: -1
  Can't make 3 with only 2s (odd amount).

Example 3:
  Input:  coins = [1], amount = 0
  Output: 0
  No coins needed for amount 0.

Example 4:
  Input:  coins = [1, 5, 10, 25], amount = 36
  Best: 25 + 10 + 1 = 3 coins.
  Output: 3

Example 5:
  Input:  coins = [186, 419, 83, 408], amount = 6249
  Output: 20

---

Constraints:
  - 1 <= coins.length <= 12
  - 1 <= coins[i] <= 2^31 - 1
  - 0 <= amount <= 10^4
"""
