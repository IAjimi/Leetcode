from typing import List


class Solution:
    def combinationSum(
        self, candidates: List[int], target: int, path=None
    ) -> List[List[int]]:
        """
        Would greatly benefit from memoization.

        Runtime: 260 ms, faster than 9.79% of Python3 online submissions for Combination Sum.
        Memory Usage: 14 MB, less than 38.36% of Python3 online submissions for Combination Sum.
        """
        if target < min(candidates):
            return []

        if not path:
            path = []

        result = []

        for i, c in enumerate(candidates):
            if target == c:
                new_path = path + [c]
                new_path.sort()  # need this for uniqueness later on
                result.append(new_path)
            elif target - c > 0:
                new_paths = self.combinationSum(candidates, target - c, path + [c])
                if new_paths:
                    result.extend(new_paths)

        return [list(x) for x in set(tuple(x) for x in result)]

    def dpCombinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Runtime: 129 ms, faster than 37.26% of Python3 online submissions for Combination Sum.
        Memory Usage: 14.6 MB, less than 8.65% of Python3 online submissions for Combination Sum.
        """
        min_candidate = min(candidates)

        # edge case: impossible to make target with candidates
        if target < min_candidate:
            return []

        solution = {0: [[]]}  # needs this to add candidates (complement = 0)

        for num in range(min_candidate, target + 1):
            for c in candidates:
                complement = num - c

                for sol in solution.get(complement, []):
                    combination = sorted([c] + sol)  # needs sorting to check uniqueness

                    if num in solution:
                        if combination not in solution[num]:
                            solution[num].append(combination)
                    else:
                        solution[num] = [combination]

        return solution.get(target, [])
