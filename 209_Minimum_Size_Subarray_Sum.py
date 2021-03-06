from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Sliding windows:
        * move right pointer as long as cum_sum < target
        * move left pointer to shrink window as long as cum_sum >= target

        Runtime: 115 ms, faster than 42.00% of Python3 online submissions for Minimum Size Subarray Sum.
        Memory Usage: 16.7 MB, less than 27.06% of Python3 online submissions for Minimum Size Subarray Sum.
        """
        if sum(nums) < target:
            return 0
        elif max(nums) >= target:
            return 1

        l = 0
        r = 1
        current_sum = nums[l] + nums[r]
        min_size = len(nums)

        while 0 <= l < r <= len(nums) - 1:
            if current_sum < target and r < len(nums) - 1:
                r += 1
                current_sum += nums[r]
            elif current_sum >= target and l < len(nums) - 1:
                min_size = min(min_size, 1 + r - l)
                current_sum -= nums[l]
                l += 1
            else:
                break

        return min_size

    def size(self, l, r):
        return 1 + r - l

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Smarter sliding window.

        Runtime: 104 ms, faster than 55.28% of Python3 online submissions for Minimum Size Subarray Sum.
        Memory Usage: 16.9 MB, less than 11.59% of Python3 online submissions for Minimum Size Subarray Sum.
        """
        if sum(nums) < target:
            return 0

        l = 0
        r = 0
        cur_sum = nums[0]
        min_size = len(nums)

        while l <= r <= len(nums) - 1:
            # shrink
            if cur_sum >= target:
                min_size = min(min_size, self.size(l, r))
                cur_sum -= nums[l]
                l += 1
            # grow
            elif cur_sum < target and self.size(l, r) + 1 < min_size:
                r += 1
                if r < len(nums):
                    cur_sum += nums[r]
            # slide
            elif cur_sum < target:
                cur_sum -= nums[l]
                l += 1
                r += 1
                if r < len(nums):
                    cur_sum += nums[r]

        return min_size


if __name__ == "__main__":
    assert Solution().minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3])
    assert Solution().minSubArrayLen(target=4, nums=[1, 4, 4]) == 1
    assert Solution().minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]) == 0
    assert Solution().minSubArrayLen(target=5, nums=[3]) == 0
    assert (
        Solution().minSubArrayLen(target=10, nums=[1, 1, 1, 1, 1, 20, 1, 1, 1, 1, 1, 1])
        == 1
    )
    assert Solution().minSubArrayLen(target=15, nums=[1, 2, 3, 4, 5]) == 5
