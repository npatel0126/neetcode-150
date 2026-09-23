"""
Idea:
Check if strings `s` and `t` have equal lengths. Use a hash map to track character frequencies 
by incrementing for characters in `s` and decrementing for characters in `t`. 
Finally, verify that all counts in the hash map are zero.

Examples:
- Input: s = "anagram", t = "nagaram" -> Output: True
- Input: s = "rat", t = "car" -> Output: False 

zip: s = "abc" and t = "xyz"

# a x
# b y
# c z

Goes through the pair of indices together

Complexity:
- Time: O(N) since we iterate through the strings of length N once.
- Space: O(U) for the hash map, where U is the number of unique characters (at most 26 for lowercase English letters).
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        for i, j in zip(s, t):
            count[i] = count.get(i, 0) + 1
            count[j] = count.get(j, 0) - 1
        
        return all(v == 0 for v in count.values())
