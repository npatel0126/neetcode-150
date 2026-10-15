"""
Idea:
Find the k most frequent elements using bucket sort (frequency bucket array). 
First, count the frequency of each number using a hash map. Then, store the numbers 
in an array of lists where the index represents the frequency (buckets from 0 to len(nums)). 
Finally, iterate through the frequency buckets from highest to lowest, collecting elements 
until we have accumulated k numbers.

Examples:
- Input: nums = [1, 1, 1, 2, 2, 3], k = 2 -> Output: [1, 2]
- Input: nums = [1], k = 1 -> Output: [1]

Complexity:
- Time: O(N) where N is the number of elements in the input array.
- Space: O(N) to store frequencies in the hash map and bucket arrays.
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
