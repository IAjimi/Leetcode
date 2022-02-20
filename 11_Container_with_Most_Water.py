from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Runtime: 856 ms, faster than 57.39% of Python3 online submissions for Container With Most Water.
        Memory Usage: 27.6 MB, less than 47.49% of Python3 online submissions for Container With Most Water.
        """
        l = 0
        r = len(height) - 1
        max_volume = 0

        while 0 <= l < r <= len(height) - 1:
            volume = min(height[l], height[r]) * abs(l - r)
            max_volume = max(max_volume, volume)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_volume


if __name__ == "__main__":
    assert 0 == Solution().maxArea([0, 1])
    assert 1 == Solution().maxArea([1, 1])
    assert 1 == Solution().maxArea([1, 2])
    assert 2 == Solution().maxArea([1, 2, 1])
    assert 24 == Solution().maxArea([1, 3, 2, 5, 25, 24, 5])
    assert 49 == Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
    assert 16 == Solution().maxArea([4, 3, 2, 1, 4])
