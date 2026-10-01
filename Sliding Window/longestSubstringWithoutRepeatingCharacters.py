"""
Idea:
Use the sliding window technique with a set to find the length of the longest substring 
without repeating characters. Expand the right boundary of the window by iterating through the string. 
If a duplicate character is encountered, shrink the window from the left until the duplicate is removed, 
then update the maximum length found.

Examples:
- Input: s = "abcabcbb" -> Output: 3 (Substring: "abc")
- Input: s = "bbbbb" -> Output: 1 (Substring: "b")

Complexity:
- Time: O(N) since each character is visited at most twice (once by the right pointer, once by the left pointer).
- Space: O(min(N, A)) where N is the length of the string and A is the size of the character set.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in seen_chars:
                seen_chars.remove(s[l])
                l += 1
            seen_chars.add(s[r])
            max_length = max(max_length, r - l + 1)
            
        return max_length
