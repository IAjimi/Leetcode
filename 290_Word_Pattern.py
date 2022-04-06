class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Runtime: 32 ms, faster than 86.09% of Python3 online submissions for Word Pattern.
        Memory Usage: 13.9 MB, less than 25.16% of Python3 online submissions for Word Pattern.
        """
        # turn into lists
        pattern = [char for char in pattern]
        s = s.split(" ")

        if len(pattern) != len(s):
            return False

        # check consistency of mapping
        hashmap = {}

        for i, word in enumerate(s):
            pattern_match = pattern[i]

            if pattern_match not in hashmap:
                hashmap[pattern_match] = word
            elif hashmap[pattern_match] != word:
                return False

        # check word uniqueness
        unique_patterns = set(hashmap.keys())
        unique_words = set(hashmap.values())
        if len(unique_words) != len(unique_patterns):
            return False

        return True
