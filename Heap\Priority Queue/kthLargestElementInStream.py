"""
Idea:
Maintain a min-heap of size k where the root is always the k-th largest element. 
During initialization, heapify the list and trim it down to size k. For each new value, 
push it to the heap, pop the smallest element if the size exceeds k, and return the root.

Examples:
- k = 3, nums = [4, 5, 8, 2] -> Initial heap keeps top 3: [4, 5, 8]
- add(3) -> Returns 4 (heap becomes [4, 5, 8])
- add(5) -> Returns 5 (heap becomes [5, 5, 8])

Complexity:
- Time: O(N log N) for initialization, and O(log k) for each add operation.
- Space: O(k) to store the k elements in the min-heap.
"""

import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = nums

        heapq.heapify(self.min_heap)
        
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)

        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]
