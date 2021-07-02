class Solution:
    def reverse(self, x: int) -> int:
        """Top 60% by speed, top 30% by memory."""
        sign = 1 if x >= 0 else -1
        x = abs(x)
        y = [c for c in str(x)][::-1]
        val = sign * int(''.join(y))
        if val > 2**31 - 1 or val < -2**31:
            return 0
        else:
            return val
        
        