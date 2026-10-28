"""
Idea:
Evaluate a Reverse Polish Notation (RPN) expression using a stack. Iterate through each token; 
if it is an operator, pop the required operands from the stack, compute the result, and push it back. 
If it is a number, convert it to an integer and push it onto the stack. Division truncates toward zero. 
The final element remaining in the stack is the evaluated result.

Examples:
- Input: tokens = ["2", "1", "+", "3", "*"] -> Output: 9
- Input: tokens = ["4", "13", "5", "/", "+"] -> Output: 6

Complexity:
- Time: O(N) where N is the number of tokens in the array, as each token is processed once.
- Space: O(N) for the stack storage.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens: 
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            else:
                stack.append(int(token))

        return stack[0]
