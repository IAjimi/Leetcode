from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Runtime: 92 ms, faster than 95.92% of Python3 online submissions for Group Anagrams.
        Memory Usage: 17.9 MB, less than 54.22% of Python3 online submissions for Group Anagrams.
        """
        sorted_strs = ["".join(sorted(s)) for s in strs]
        zipped = zip(strs, sorted_strs)

        hashmap = defaultdict(list)

        for string, sorted_string in zipped:
            hashmap[sorted_string].append(string)

        return hashmap.values()


if __name__ == "__main__":
    assert Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])
