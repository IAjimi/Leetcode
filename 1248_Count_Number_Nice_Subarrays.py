from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        """
        Runtime: 1103 ms, faster than 54.93% of Python3 online submissions for Count Number of Nice Subarrays.
        Memory Usage: 20.9 MB, less than 72.40% of Python3 online submissions for Count Number of Nice Subarrays.

        * j is current pointer
        * l is smallest i s.t. A[l:k] meets condition
        * r is largest i s.t. A[r:k] meets condition

        Example 1:
            #   1 1 2 1 1  k=3  (nums)
            # 0 1 2 3 4 5  (index)
            # 0 1 2 2 3 3  (prefix sum P)
            # l r     j    <- ans += r - l = 1
            # l r       j  <- ans += r - l = 1

        Example 2:
            #   2 2 2 1 2 2 1 2 2 2   k=2  (nums)
            # 0 1 2 3 4 5 6 7 8 9 10 (index)
            # 0 0 0 0 1 1 1 2 2 2 2  (prefix sum P)
            # l       r     j        <- ans += 4
            # l       r       j      <- ans += 4
            # l       r         j    <- ans += 4
            # l       r           j  <- ans += 4
        """
        # prefix sum
        P = [0]
        counter = 0
        for i, n in enumerate(nums):
            if n % 2 != 0:
                counter += 1

            P.append(counter)

        # i, low pointers
        sol = 0
        l, r = 0, 0

        for j in range(1, len(nums) + 1):
            while P[j] - P[l] > k and l < j:
                l += 1

            while P[j] - P[r] >= k and r < j:
                r += 1

            sol += r - l

        return sol
