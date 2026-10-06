"""
Idea:
Use bottom-up dynamic programming to find the fewest number of coins needed to make up a given amount. 
Initialize an array of size `amount + 1` with a placeholder value greater than the target amount (e.g., `amount + 1`), 
setting `min_coins[0] = 0`. For each amount from 1 up to the target, iterate through each coin and update the minimum coins 
required by checking `1 + min_coins[amount - coin]`.

Examples:
- Input: coins = [1, 2, 5], amount = 11 -> Output: 3 (5 + 5 + 1)
- Input: coins = [2], amount = 3 -> Output: -1

Complexity:
- Time: O(amount * N) where amount is the target value and N is the number of coins.
- Space: O(amount) for the array storage.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [amount + 1] * (amount + 1)
        min_coins[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    min_coins[a] = min(min_coins[a], 1 + min_coins[a - c])
            
        return min_coins[amount] if min_coins[amount] != amount + 1 else -1
