from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Faster implementation would probably be dumping nums 2 at the end of nums 1 and
        sorting the array.

        Process here is as follows:
            1 2 5 0 0 0 | 2 4 7
            l             r     <- l <= r, so move l by 1
              l           r
                l         r     <- l > r, so shift all elements in nums1 >= r and move nums2[r] in nums1[l]
            1 2 2 5 0 0 | 2 4 7 <- increment both pointers by 1
                  l         r
            1 2 2 4 5 0 | 2 4 7
                    l         r

            We've hit the end of nums1 (while taking into account the elements we added to it),
            so we copy over all elements of nums2 at index >= r to nums1.

            -> 1 2 2 4 5 7


        Runtime: 68 ms, faster than 17.83% of Python3 online submissions for Merge Sorted Array.
        Memory Usage: 14 MB, less than 79.94% of Python3 online submissions for Merge Sorted Array.
        """
        l = 0
        r = 0
        n_moved = 0  # number of elements in nums2 moved to nums1

        while l <= m - 1 + n_moved and r <= n - 1:
            if nums1[l] <= nums2[r]:
                l += 1
            else:
                # shift nums1 to make place for element of nums2
                for i in range(m + n_moved - 1, l - 1, -1):
                    nums1[i + 1] = nums1[i]
                nums1[l] = nums2[r]
                l += 1
                r += 1
                n_moved += 1

        while r <= n - 1:
            nums1[l] = nums2[r]
            l += 1
            r += 1


if __name__ == "__main__":
    assert Solution().merge(nums1=[0], m=0, nums2=[1], n=1) == [1]
    assert Solution().merge(nums1=[1], m=1, nums2=[], n=0) == [1]
    assert Solution().merge(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [
        1,
        2,
        2,
        3,
        5,
        6,
    ]
    assert Solution().merge(nums1=[7, 8, 9, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) == [
        2,
        5,
        6,
        7,
        8,
        9,
    ]
