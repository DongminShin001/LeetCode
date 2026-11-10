"""
#20 — Valid Parentheses | Easy | Companies: Amazon, Google, Meta, Microsoft, Bloomberg (Everywhere)

Given a string `s` containing only the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

A string is valid if:
  1. Open brackets are closed by the same type of bracket.
  2. Open brackets are closed in the correct order.
  3. Every closing bracket has a corresponding open bracket.

Examples:
  s = "()"        ->  true
  s = "()[]{}"    ->  true
  s = "(]"        ->  false
  s = "([)]"      ->  false
  s = "{[]}"      ->  true

Constraints:
  - 1 <= s.length <= 10^4
  - s consists of parentheses only: '()[]{}'
"""
