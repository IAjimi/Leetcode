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

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Using a hashtable (Python dict) for quick lookup of values.

        Runtime: 60 ms, faster than 76.38% of Python3 online submissions.
        Memory Usage: 16.3 MB, less than 9.35% of Python3 online submissions.
        """
        hashtable = {}
        for ix in range(len(nums)):
            if nums[ix] in hashtable:
                hashtable[nums[ix]].append(ix)
            else:
                hashtable[nums[ix]] = [ix]

        for ix in range(len(nums)):
            val = nums[ix]
            complement = target - val
            if complement != val and complement in hashtable:
                return [ix, hashtable[complement][0]]
            elif complement == val and len(hashtable[val]) > 1:
                return hashtable[complement][:2]