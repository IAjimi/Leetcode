class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        """
        Dynamic programming approach. (Could refactor to use O(1) space and have less columns.)

        Ex. self.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])
        creates dp matrix where rows are different jobs, and columns are end times
               0  1  2  3  4  5  6
            1  0  0  0 50 50 50 50  <- starts at 1, ends at 3, 50 profit once completed
            2  0  0  0 50 50 50 50  <- starts at 2, ends at 4, only 10 profit so previous job is better
            3  0  0  0 50 50 90 90  <- starts at 3, ends at 5, 90 profit = 40 for this job + 50 from job 1
            4  0  0  0 50 50 90 120 <- starts at 3, ends at 6, 120 profit = 70 for this job + 50 from job 1
        """
        jobs = sorted(zip(startTime, endTime, profit))
        dp = [[0] * (max(endTime) + 1) for _ in range(len(jobs))]

        for ix, job in enumerate(jobs):
            start, end, reward = job
            dp[ix] = dp[ix - 1][:]

            for t in range(end, max(endTime) + 1):
                # dp[ix - 1][start] is max profit possible at start of job + reward from completing this job
				# dp[ix][t] is alternative (not doing job)
                dp[ix][t] = max(dp[ix - 1][start] + reward, dp[ix][t])

        return dp[-1][-1]

if __name__ == '__main__':
    assert 120 == Solution().jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70])
    assert 150 == Solution().jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])
    assert 6 == Solution().jobScheduling([1,1,1], [2,3,4], [5,6,4])
    assert 7 == Solution().jobScheduling([1,2,2,3], [2,5,3,4]	, [3,4,1,2])
    assert 18 == Solution().jobScheduling([4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4])
    assert 41 == Solution().jobScheduling([6, 15, 7, 11, 1, 3, 16, 2], [19, 18, 19, 16, 10, 8, 19, 8], [2, 9, 1, 19, 5, 7, 3, 19])



