class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Note: paths should actually be initialized at 1. The first row will always be
        only 1s, so can do range(1, n), range(1, m) instead.
        Note 2: can also just use 1 array instead of a matrix!

        Runtime: 36 ms, faster than 28.89% of Python3 online submissions.
        Memory Usage: 14.3 MB, less than 65.63% of Python3 online submissions.
        """
        if m == 1 or n == 1:
            return 1
        else:
            paths = [[0] * n for i in range(m)]
            paths[0][0] = 0
            paths[0][1] = 1
            paths[1][0] = 1

            for ix in range(n):
                for jx in range(m):
                    if (jx, ix) not in [(0, 0), (0, 1), (1, 0)]:
                        paths[jx][ix] = max(paths[jx - 1][ix] + paths[jx][ix - 1], paths[jx][ix])

            return paths[-1][-1]
