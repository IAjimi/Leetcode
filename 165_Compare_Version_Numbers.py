import itertools


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        """
        Runtime: 38 ms, faster than 62.44% of Python3 online submissions for Compare Version Numbers.
        Memory Usage: 13.9 MB, less than 92.33% of Python3 online submissions for Compare Version Numbers.
        """
        v1 = [int(s) for s in version1.split(".")]
        v2 = [int(s) for s in version2.split(".")]

        for v1_num, v2_num in itertools.zip_longest(v1, v2, fillvalue=0):
            if v1_num > v2_num:
                return 1
            elif v1_num < v2_num:
                return -1

        return 0
