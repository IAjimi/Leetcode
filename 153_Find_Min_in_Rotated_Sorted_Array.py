class Solution:
    def findMin(self, nums):
        """
        Binary search type thing.

        Runtime: 44 ms, faster than 39.47% of Python3 online submissions.
		Memory Usage: 14.7 MB, less than 28.49% of Python3 online submissions.
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        else:
            left, right = 0, len(nums) - 1

            while right - left > 1:  # can get stuck for odd numbered arrays
                if nums[right] >= nums[left]:
                    right = (right + left) // 2
                else:
                    left = (right + left) // 2

            while nums[left] > nums[left - 1]:
                left += -1

            return nums[left]

if __name__ == '__main__':
    assert 0 == Solution().findMin([0])
    assert 1 == Solution().findMin([1,2])
    assert 1 == Solution().findMin([2,1])
    assert 1 == Solution().findMin([3,1,2])
    assert 1 == Solution().findMin([2,3,1])
    assert 1 == Solution().findMin([3,4,5,1,2])
    assert 0 == Solution().findMin([4,5,6,7,0,1,2])
    assert 11 == Solution().findMin([11,13,15,17])