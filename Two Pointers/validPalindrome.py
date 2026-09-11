"""
Idea:
Use two pointers starting at opposite ends of the string and moving inward. 
Skip any non-alphanumeric characters. Compare the lowercase versions of the 
characters at both pointers; return False if they do not match.

Examples:
- Input: s = "A man, a plan, a canal: Panama" -> Output: True
- Input: s = "race a car" -> Output: False

Complexity:
- Time: O(N) since we traverse the string at most once.
- Space: O(1) using only two pointer variables.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                 l += 1
                 continue 
            
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        
        return True
