from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Runtime: 758 ms, faster than 70.28% of Python3 online submissions for Gas Station.
        Memory Usage: 19.4 MB, less than 28.78% of Python3 online submissions for Gas Station.
        """
        total_gas = 0
        pos = 0
        tank = 0

        for i, (gas, cost) in enumerate(zip(gas, cost)):
            tank += gas - cost
            total_gas += gas - cost

            if tank < 0:
                tank = 0
                pos = i + 1

        if total_gas < 0:
            return -1
        else:
            return pos
