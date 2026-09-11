"""
Idea:
Use a stack to track opening brackets. When encountering a closing bracket, 
check if the stack is non-empty and its top matches the corresponding opening bracket. 
If it does not match or the stack is empty, return False. Finally, return True only if the stack is empty.

Examples:
- Input: s = "()[]{}" -> Output: True
- Input: s = "([)]" -> Output: False

Complexity:
- Time: O(N) because we iterate through the string of length N once.
- Space: O(N) to store the stack in the worst case.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {')':'(', ']':'[', '}':'{'}
        stack = []
        
        for bracket in s:
            if bracket not in hashmap:
                stack.append(bracket)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != hashmap[bracket]:
                        return False
        
        return not stack
