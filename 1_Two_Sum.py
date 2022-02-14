from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {n: i for i, n in enumerate(nums)}

        for j, m in enumerate(nums):
            missing_sum = target - m
            if missing_sum in d and d[missing_sum] != j:
                return [j, d[missing_sum]]
