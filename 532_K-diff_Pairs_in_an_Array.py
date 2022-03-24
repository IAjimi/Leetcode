from collections import defaultdict
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        """
        Runtime: 179 ms, faster than 11.64% of Python3 online submissions for K-diff Pairs in an Array.
        Memory Usage: 19.6 MB, less than 5.01% of Python3 online submissions for K-diff Pairs in an Array.
        """
        solution = set()

        # 1. Create a hashmap, number -> index
        targets = defaultdict(set)

        for ix, val in enumerate(nums):
            targets[val].add(ix)

        # 2. Iterate over nums once
        for i, val in enumerate(nums):
            matching = val - k, val + k

            for j in targets.get(matching[0], set()):
                if j > i:
                    solution.add((matching[0], val))  # matching < val

            for j in targets.get(matching[1], set()):
                if j > i:
                    solution.add((val, matching[1]))  # matching > val

        return len(solution)


if __name__ == "__main__":
    assert Solution().findPairs(nums=[1], k=0) == 0
    assert Solution().findPairs(nums=[1, 1], k=0) == 1
    assert Solution().findPairs(nums=[3, 1, 4, 1, 5], k=2) == 2
    assert Solution().findPairs(nums=[1, 2, 3, 4, 5], k=1) == 4
    assert Solution().findPairs(nums=[1, 3, 1, 5, 4], k=0) == 1
    assert Solution().findPairs(nums=[1, 2, 4, 4, 3, 3, 0, 9, 2, 3], k=3) == 2
