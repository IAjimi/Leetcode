from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """Runtime: 865 ms, faster than 40.25% of Python3 online submissions for Contains Duplicate II.
        Memory Usage: 44 MB, less than 5.31% of Python3 online submissions for Contains Duplicate II."""

        # creating hashmap
        hashmap = defaultdict(set)

        for i, n in enumerate(nums):
            hashmap[n].add(i)

        # iterate over nums
        for i, n in enumerate(nums):
            if n in hashmap:
                for j in hashmap[n]:
                    if i != j and abs(i - j) <= k:
                        return True

        return False

if __name__ == '__main__':
    assert not Solution().containsNearbyDuplicate(nums=[1], k=0)
    assert not Solution().containsNearbyDuplicate(nums=[1, 2], k=0)
    assert Solution().containsNearbyDuplicate(nums=[1, 2, 1], k=2)
    assert not Solution().containsNearbyDuplicate(nums=[1, 2, 1], k=1)

    assert Solution().containsNearbyDuplicate(nums=[1,0,1,1], k=3)
    assert Solution().containsNearbyDuplicate(nums=[1,0,1,1], k=1)
    assert not Solution().containsNearbyDuplicate(nums=[1,2,3,1,2,3], k=2)