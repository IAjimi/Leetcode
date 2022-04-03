from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Runtime: 700 ms, faster than 61.81% of Python3 online submissions for Max Consecutive Ones III.
        Memory Usage: 15.1 MB, less than 7.35% of Python3 online submissions for Max Consecutive Ones III.
        """
        # Edge case: all 0s, k == 0
        if sum(nums) == 0 and k == 0:
            return 0

        l = 0
        r = l + 1
        max_length = 0
        zeros = []  # ix of 0s

        if nums[l] == 0:
            zeros.append(l)

        while 0 <= l < r <= len(nums) - 1:
            # update 0s if relevant
            if nums[r] == 0:
                zeros.append(r)

            # while not hit k 0s, move r right
            if len(zeros) <= k:
                r += 1
            # if hit k 0s, record max, set l to neighbor of oldest 0
            else:
                max_length = max(max_length, r - l)
                l = zeros.pop(0)  # move right of 1st zero
                l += 1

                # need to update 0 if left pointer is in another 0!
                if l <= len(nums) - 1 and nums[l] == 0 and l not in zeros:
                    zeros.append(l)

                r = r + 1 if r > l else l + 1

        max_length = max(max_length, r - l)
        return max_length


if __name__ == "__main__":
    assert Solution().longestOnes(nums=[0], k=0) == 0
    assert Solution().longestOnes(nums=[1], k=0) == 1
    assert Solution().longestOnes(nums=[0], k=1) == 1
    assert Solution().longestOnes(nums=[1, 0], k=0) == 1
    assert Solution().longestOnes(nums=[1, 1], k=0) == 2
    assert Solution().longestOnes(nums=[1, 0, 1], k=0) == 1
    assert Solution().longestOnes(nums=[1, 1, 1], k=1) == 3

    assert Solution().longestOnes(nums=[0, 0, 0], k=0) == 0
    assert Solution().longestOnes(nums=[0, 0, 0], k=1) == 1
    assert Solution().longestOnes(nums=[0, 0, 0], k=2) == 2

    assert Solution().longestOnes(nums=[1, 0, 1, 1], k=1) == 4
    assert Solution().longestOnes(nums=[1, 0, 1, 1, 0], k=1) == 4
    assert Solution().longestOnes(nums=[1, 0, 0, 1, 1, 1, 0, 1, 1], k=0) == 3

    assert (
        Solution().longestOnes(
            nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=1
        )
        == 6
    )
    assert (
        Solution().longestOnes(
            nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=2
        )
        == 7
    )
    assert (
        Solution().longestOnes(
            nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3
        )
        == 10
    )
    assert (
        Solution().longestOnes(
            nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=4
        )
        == 13
    )
    assert (
        Solution().longestOnes(
            nums=[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=5
        )
        == 14
    )
