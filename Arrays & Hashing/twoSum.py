"""
Idea:
Use a hash map to store each number and its index as we iterate through the array. 
For each number, calculate its complement (target - num). If the complement 
already exists in the hash map, return its index along with the current index. 
Otherwise, store the current number and index in the map.

Examples:
- Input: nums = [2, 7, 11, 15], target = 9 -> Output: [0, 1]
- Input: nums = [3, 2, 4], target = 6 -> Output: [1, 2]

Complexity:
- Time: O(N) since we traverse the list of length N once with O(1) hash map lookups.
- Space: O(N) to store the elements in the hash map.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffMap:
                return [diffMap[diff], i]
            else:
                diffMap[num] = i
