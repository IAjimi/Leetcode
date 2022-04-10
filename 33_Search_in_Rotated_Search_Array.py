import random
import math
from typing import List


class Solution:
    def search(self, nums, target):
        """
        Idea: if array is pivoted, run binary search to find the pivot and adjust l/r accordingly.
        Then run a binary search of the relevant array.

        Runtime: 32 ms, faster than 97.82% of Python3 online submissions for Search.
        Memory Usage: 14.7 MB, less than 23.69% of Python3 online submissions for Search.
        """
        l, r = 0, len(nums) - 1

        # Check ends (useful for length 1 arrays)
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r

        # Array was rotated
        if nums[l] > nums[r]:
            # Find pivot
            while l < r - 1:
                mid = (l + r) // 2

                # Pivot is to the left
                if nums[mid] < nums[l]:
                    r = mid
                else:
                    l = mid

                # Check for target while we're at it
                if nums[mid] == target:
                    return mid
                if nums[l] == target:
                    return l
                if nums[r] == target:
                    return r

            # Adjust l/r based on target
            if nums[0] <= target <= nums[l]:
                l, r = 0, l
            elif nums[l + 1] <= target <= nums[len(nums) - 1]:
                l, r = l + 1, len(nums) - 1

        # Binary search in relevant sub-array
        while l < r - 1:
            mid = math.ceil((l + r) / 2)

            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            elif target == nums[mid]:
                return mid
            elif nums[l] < target < nums[mid]:
                r = mid
            elif nums[mid] < target < nums[r]:
                l = mid
            else:
                return -1

        return -1

    def onePassSearch(self, nums: List[int], target: int) -> int:
        """
        Runtime: 75 ms, faster than 21.43% of Python3 online submissions for Search in Rotated Sorted Array.
        Memory Usage: 14.2 MB, less than 59.93% of Python3 online submissions for Search in Rotated Sorted Array.
        """
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            sorted_subarray = nums[l] < nums[r]

            if nums[m] == target:
                return m
            # whole subarray sorted
            elif sorted_subarray:
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            # leftside sorted
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # rightside sorted
            else:
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


def generate_rotated_search_array(length):
    """
    Create a random sorted array of length length, pivoted randomly.
    """
    # Create random sorted array
    nums = random.sample(range(0, length * 2), length)
    nums.sort()

    # Pivot
    pivot = random.randint(0, length)
    return nums[pivot:] + nums[:pivot]


def test_search(length):
    """
    Test the solution with a random rotated search array.
    """
    nums = generate_rotated_search_array(length)
    search_element = random.randint(
        0, length * 2
    )  # length * 2 so nums are sometimes not in array
    try:
        solution = nums.index(search_element)
    except:
        solution = -1
    print(f"Looking for {search_element} in {nums} - solution is {solution}.")
    assert solution == Solution().search(nums, search_element)


if __name__ == "__main__":
    # Length 1 arrays
    assert 0 == Solution().search([0], 0)
    assert -1 == Solution().search([0], 1)
    assert -1 == Solution().search([1], 0)

    # Sample sorted arrays
    assert 1 == Solution().search([0, 1, 3, 8, 9], 1)

    # Sample pivoted arrays
    assert 2 == Solution().search([4, 7, 0], 0)
    assert -1 == Solution().search([4, 7, 0], 1)
    assert 4 == Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
    assert -1 == Solution().search([4, 5, 6, 7, 0, 1, 2], 3)
    assert 2 == Solution().search([1, 2, 3, 4, 5, 6, 7, 0], 3)
    assert 3 == Solution().search([17, 19, 2, 3, 6, 8, 11, 12, 13, 15], 3)
    assert 8 == Solution().search([22, 0, 2, 5, 6, 10, 12, 13, 14, 16, 17, 21], 14)
