"""
Idea:
Use a max-heap (implemented in Python by negating values) to repeatedly smash the two heaviest stones. 
Pop the two largest elements, and if they are not equal, push the absolute difference back into the heap. 
Repeat until 1 or 0 stones remain, then return the remaining weight.

Examples:
- Input: stones = [2, 7, 4, 1, 8, 1] -> Output: 1
- Input: stones = [1] -> Output: 1

Complexity:
- Time: O(N log N) because each heap operation takes O(log N) and is performed for each stone.
- Space: O(N) to store the elements in the heap.
"""

import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones] #since python by default implements min heap, this is used to preserve the max heap 
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)  #heaviest stone
            second = heapq.heappop(stones) #second heaviest stone
            
            if second > first:             
                heapq.heappush(stones, first - second)
                
        return abs(stones[0]) if stones else 0
