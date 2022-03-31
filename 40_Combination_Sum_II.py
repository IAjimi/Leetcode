from typing import List


class Solution:
    def handler(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        elif min(candidates) > target:
            return []

        result = []
        for i, c in enumerate(candidates):
            # avoid duplicates
            if i > 0 and c == candidates[i - 1]:
                continue
            elif target - c == 0:
                result.append([c])
            else:
                new_results = self.combinationSum2(candidates[i + 1 :], target - c)
                new_results = [[c] + r for r in new_results]
                result.extend(new_results)

        return result

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Runtime: 111 ms, faster than 42.97% of Python3 online submissions for Combination Sum II.
        Memory Usage: 14 MB, less than 60.40% of Python3 online submissions for Combination Sum II.
        """
        candidates.sort()  # only need to sort once

        result = self.handler(candidates, target)
        return result
