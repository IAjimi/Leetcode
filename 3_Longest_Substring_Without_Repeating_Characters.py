from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        """
        Runtime: 52 ms, faster than 91.76% of Python3 online submissions.
        Memory Usage: 14.2 MB, less than 80.56% of Python3 online submissions.
        """
        if len(string) == 0:
            return 0

        l = 0
        max_length = 0
        substring = {}

        for ix in range(len(string)):
            s = string[ix]
            if s not in substring:
                substring[s] = ix
                max_length = max(ix - l + 1, max_length)
            else:
                if l <= substring[s]:
                    l = substring[s] + 1
                else:
                    max_length = max(ix - l + 1, max_length)
                substring[s] = ix

        return max_length

    def slidingWindowLengthOfLongestSubstring(self, s: str) -> int:
        """
        Runtime: 199 ms, faster than 21.42% of Python3 online submissions for Longest Substring Without Repeating Characters.
        Memory Usage: 14 MB, less than 76.14% of Python3 online submissions for Longest Substring Without Repeating Characters.
        """
        letters = defaultdict(int)
        max_length = 0
        l = 0
        r = 0

        while 0 <= l <= r <= len(s) - 1:
            cur_char = s[r]
            letters[cur_char] += 1

            # update letters, move l, r to right
            if max(letters.values()) > 1:
                letters[s[l]] -= 1
                l += 1
                r += 1
            # update length, letters, move r to the right
            else:
                max_length = max(max_length, 1 + r - l)
                r += 1

        return max_length


if __name__ == "__main__":
    assert 3 == Solution().lengthOfLongestSubstring("abcabcbb")
    assert 1 == Solution().lengthOfLongestSubstring("bbbbb")
    assert 3 == Solution().lengthOfLongestSubstring("pwwkew")
    assert 0 == Solution().lengthOfLongestSubstring("")
    assert 5 == Solution().lengthOfLongestSubstring("tmmzuxt")
    assert 4 == Solution().lengthOfLongestSubstring("aaaabcda")
