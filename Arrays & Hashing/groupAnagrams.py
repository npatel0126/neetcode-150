"""
Idea:
Group anagrams together by using the frequency count of 26 lowercase English letters as a unique key in a standard dictionary. 
For each string, compute its character count array, convert it into a tuple, and check if the key exists in the dictionary. 
If not, initialize it with an empty list before appending the original string. Finally, return all values as a list.

Examples:
- Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"] 
  -> Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]] (or any order)
- Input: strs = [""] -> Output: [[""]]

Complexity:
- Time: O(N * K) where N is the number of strings and K is the maximum length of a string.
- Space: O(N * K) to store the grouped strings in the dictionary.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = {}

        for s in strs:
            count = [0] * 26  # Each index represents a letter from 'a' to 'z'

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            key = tuple(count)
            if key not in anagram_map:
                anagram_map[key] = []
            
            anagram_map[key].append(s)
        
        return list(anagram_map.values())


# Solution using default dict in python, so the edge case of a key not exisiting does not need to be checked
    def groupAnagramsTwo(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26  # Each index represents a letter from 'a' to 'z'

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            anagram_map[tuple(count)].append(s)
        
        return list(anagram_map.values()
