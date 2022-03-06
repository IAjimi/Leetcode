from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Runtime: 452 ms, faster than 76.62% of Python3 online submissions for Contains Duplicate.
        Memory Usage: 26.1 MB, less than 5.23% of Python3 online submissions for Contains Duplicate."""
        hashMap = set()

        for n in nums:
            if n in hashMap:
                return False
            else:
                hashMap.add(n)

        return True


if __name__ == "__main__":
    assert not Solution().containsDuplicate([1])
    assert not Solution().containsDuplicate([1, 2])
    assert Solution().containsDuplicate([1, 2, 1])
