class NumArray:
    """
    Runtime: 68 ms, faster than 97.72% of Python3 online submissions.
    Memory Usage: 17.7 MB, less than 47.05% of Python3 online submissions.
    """

    def __init__(self, nums):
        self.cum_sum = nums[:]
        for ix in range(1, len(self.cum_sum)):
            self.cum_sum[ix] += self.cum_sum[ix - 1]

    def sumRange(self, left, right):
        return (
            self.cum_sum[right] - self.cum_sum[left - 1]
            if left - 1 >= 0
            else self.cum_sum[right]
        )


class easyNumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        return sum(self.nums[left : right + 1])


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, -1]
    obj = NumArray(nums)

    for left in range(len(nums)):
        for right in range(left, len(nums)):
            assert sum(nums[left : right + 1]) == obj.sumRange(left, right)
