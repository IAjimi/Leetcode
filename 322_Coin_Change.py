class Solution:
    def coinChange(self, coins, amount):
        """
        Runtime: 1462 ms, faster than 53.27% of Python3 online submissions.
        Memory Usage: 14.5 MB, less than 64.64% of Python3 online submissions.
        """
        # Check to see if possible
        if amount != 0 and min(coins) > amount:
            return -1

        # Initialize change
        change = [99999 for _ in range(amount + 1)]
        change[0] = 0

        # Find optimum
        for coin in range(1, amount + 1):
            if coin in coins:
                change[coin] = 1
            else:
                relevant_coins = [c for c in coins if c <= coin]
                if relevant_coins:
                    change[coin] = min([1 + change[coin - c] for c in relevant_coins])

        return change[-1] if change[-1] < 99999 else -1


if __name__ == "__main__":
    assert 3 == Solution().coinChange(coins=[1, 2, 5], amount=11)
    assert -1 == Solution().coinChange(coins=[2], amount=3)
    assert 1 == Solution().coinChange(coins=[1], amount=1)
    assert 2 == Solution().coinChange(coins=[1], amount=2)
    assert 0 == Solution().coinChange(coins=[1], amount=0)  # check amount=0
    assert -1 == Solution().coinChange(coins=[2147483647], amount=2)
    assert 2 == Solution().coinChange(coins=[1, 2147483647], amount=2)
