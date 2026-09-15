"""
Idea:
Track the minimum price seen so far while iterating through the array. 
For each price, calculate the potential profit if sold today, and update 
the maximum profit if it exceeds the current record.

Examples:
- Input: prices = [7, 1, 5, 3, 6, 4] -> Output: 5
- Input: prices = [7, 6, 4, 3, 1] -> Output: 0

Complexity:
- Time: O(N) since we traverse the price list of length N once.
- Space: O(1) using constant extra space for tracking variables.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit
