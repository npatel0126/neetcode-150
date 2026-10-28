"""
Idea:
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. 
Use an auxiliary stack (`min_stack`) alongside the main stack to keep track of the minimum value at every level. 
Whenever a value is pushed, push the minimum of the current value and the current top of the `min_stack` onto it.

Examples:
- min_stack = MinStack()
  min_stack.push(-2)
  min_stack.push(0)
  min_stack.push(-3)
  min_stack.getMin() -> returns -3
  min_stack.pop()
  min_stack.top()    -> returns 0
  min_stack.getMin() -> returns -2

Complexity:
- Time: O(1) for all stack operations (push, pop, top, getMin).
- Space: O(N) where N is the number of elements in the stack, used by the auxiliary minimum stack.
"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
