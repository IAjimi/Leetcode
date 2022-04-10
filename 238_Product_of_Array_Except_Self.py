from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Runtime: 256 ms, faster than 33.85% of Python3 online submissions.
        Memory Usage: 21.5 MB, less than 40.58% of Python3 online submissions.

        Idea: create two arrays, do cumulative product from left and right over them.
        Example:
                nums = [2, 3, 4, 5]

                start by left at 2nd element:
                left = [1, (1), 1, 1], left[ix - 1] = 1, nums[ix - 1] = 2
                left = [1, 2, (1), 1], left[ix - 1] = 2, nums[ix - 1] = 3
                left = [1, 2, 6, (1)], left[ix - 1] = 6, nums[ix - 1] = 4
                left = [1, 2, 6, 24]

                then do right at next-to-last element:
                right = [1, 1, (1), 1], right[ix + 1] = 1, nums[ix + 1] = 5
                right = [1, (1), 5, 1], right[ix + 1] = 5, nums[ix + 1] = 4
                right = [(1), 20, 5, 1], right[ix + 1] = 20, nums[ix + 1] = 3
                right = [60, 20, 5, 1]

                then nums[ix] = left[ix] * right[ix]

                nums = [60, 40, 30, 24]
        """
        left = [1 for n in nums]
        right = [1 for n in nums]

        for ix in range(1, len(nums)):
            left[ix] = left[ix - 1] * nums[ix - 1]

        for ix in range(len(nums) - 2, -1, -1):
            right[ix] = right[ix + 1] * nums[ix + 1]

        for ix in range(len(nums)):
            nums[ix] = left[ix] * right[ix]

        return nums

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Mild rewrite for speed (using 2 pointers instead of 2 for loops).

        Runtime: 248 ms, faster than 46.67% of Python3 online submissions.
        Memory Usage: 21.4 MB, less than 40.58% of Python3 online submissions.
        """
        left = [1 for n in nums]
        right = [1 for n in nums]

        l, r = 1, len(nums) - 2

        while l <= len(nums) - 1 and r >= 0:
            left[l] = left[l - 1] * nums[l - 1]
            right[r] = right[r + 1] * nums[r + 1]
            l += 1
            r += -1

        for ix in range(len(nums)):
            nums[ix] = left[ix] * right[ix]

        return nums


if __name__ == "__main__":
    assert Solution().productExceptSelf([1, 1]) == [1, 1]
    assert Solution().productExceptSelf([2, 3]) == [3, 2]
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
