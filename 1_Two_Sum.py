class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ix in range(len(nums)):
            missing_n = target - nums[ix]
            other_nums = nums[:ix] + nums[ix+1:]
            if missing_n in other_nums:
                jx = other_nums.index(missing_n)
                jx = jx if jx < ix else jx + 1
                result = [ix, jx]
                return result