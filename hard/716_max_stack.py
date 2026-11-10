"""
716. Max Stack
Difficulty: Hard
Companies: Google

Problem:
Design a max stack that supports:
  - push(x): Push element x onto the stack.
  - pop(): Remove and return the top element.
  - top(): Return the top element without removing it.
  - peekMax(): Return the maximum element without removing it.
  - popMax(): Remove and return the maximum element. If multiple max elements,
    remove the topmost one.

Examples:

1. push(5), push(1), push(5)
   Stack (bottom to top): [5, 1, 5]
   peekMax() -> 5  (max is 5)
   pop()     -> 5  (remove top)
   Stack: [5, 1]
   top()     -> 1
   popMax()  -> 5  (removes the max, which is now 5 at bottom)
   Stack: [1]

2. push(2), push(2)
   Stack: [2, 2]
   popMax() -> 2  (topmost max removed)
   Stack: [2]
   pop()    -> 2
   Stack: []

3. push(-1), push(-2), push(-3)
   Stack: [-1, -2, -3]
   peekMax() -> -1  (least negative = max)
   popMax()  -> -1  (removes -1 at bottom since it's max)
   Stack: [-2, -3]

4. push(10), push(20), push(10), push(20)
   Stack: [10, 20, 10, 20]
   popMax() -> 20  (topmost 20, at index 3)
   Stack: [10, 20, 10]
   popMax() -> 20  (now topmost max is 20 at index 1... but 10 is on top)
   Remove from middle: stack -> [10, 10]

5. push(1), push(3), push(2)
   top()     -> 2
   peekMax() -> 3
   pop()     -> 2
   peekMax() -> 3
   popMax()  -> 3
   top()     -> 1
"""
