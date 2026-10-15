"""
Idea:
Encode a list of strings into a single string by prefixing each string with its length followed by a delimiter (`?`). 
Decode the string by iterating through it, reading the length prefix before each delimiter, and extracting the exact 
substring of that length.

Examples:
- Input: ["lint", "code", "love", "you"] -> Output: ["lint", "code", "love", "you"]
- Input: ["we", "say", ":", "yes"] -> Output: ["we", "say", ":", "yes"]

Complexity:
- Time: O(N) where N is the total number of characters across all strings in the input, as each character is processed once during encoding and decoding.
- Space: O(N) to store the encoded string and the resulting decoded list.
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + ":" + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != ":":
                j += 1
            length = int(s[i:j])  
            decoded_list.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length  
        return decoded_list
