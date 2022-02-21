from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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
