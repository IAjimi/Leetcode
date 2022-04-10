class Solution:
    def increasingTriplet(self, nums):
        """
        Uses 3 pointers, moving around.

        Runtime: 546 ms, faster than 97.24% of Python3 online submissions.
        Memory Usage: 24.5 MB, less than 99.19% of Python3 online submissions.

        Example:
                [2, 1, 9, 5, 4, 6]
                >i  j  k
                >   i  j  k           <- nums[j] < nums[i], so we move i to j's position
                >   i     j  k        <- nums[i] < nums[k] < nums[j] so we move j to k and k forward
                >   i        j  k     <- nums[i] < nums[k] < nums[j] so we move j to k and k forward

        Another Example:
                [7, 9, 1, 1, 3, 9, 0, 9]
                >i  j  k
                >i  j           k        <- nums[k] < nums[j] throughout
                >i              j  k     <- nums[i] < nums[k] < nums[j] so we move j to k and k forward
                >i              j     k  <- hit the end, j and k will be reset near i + 1
                >   i  j  k              <- nums[j] < nums[i] so we move i to j
                >      i  j  k           <- above, again
                >         i  j  k        <- found our triplet

        """
        if len(nums) < 3:
            return False
        else:
            # Sanity check: are there 3 distinct values in nums?
            if len(set(nums)) < 3:
                return False

            # If so, proceed
            i, j, k = 0, 1, 2

            while i < j < k <= len(nums) - 1:
                if nums[i] < nums[j] < nums[k]:
                    return True
                elif nums[i] >= nums[j]:
                    i = j  # move i to this new minimum
                    j = k
                    k = j + 1
                elif nums[j] >= nums[k]:
                    j = (
                        k if nums[k] > nums[i] else j
                    )  # move j to this intermediary value (nums[i] < nums[k] <= nums[j])
                    k += 1

                # K reached the end, but we can still move i rightwards
                if k > len(nums) - 1 and i < len(nums) - 3:
                    i += 1
                    j = i + 1
                    k = j + 1

            return False


def test(r):
    """
    Generates test cases.
    """
    import random

    n = [random.randint(0, 10) for _ in range(r)]
    print(n, Solution().increasingTriplet(n))


if __name__ == "__main__":
    # Not enough numbers
    assert not Solution().increasingTriplet([1])
    assert not Solution().increasingTriplet([1, 2])

    # Single triplet
    assert not Solution().increasingTriplet([1, 2, 0])
    assert Solution().increasingTriplet([1, 2, 3])
    assert not Solution().increasingTriplet([3, 2, 1])
    assert not Solution().increasingTriplet([2, 2, 2])

    # Medium Length
    assert not Solution().increasingTriplet([8, 5, 4, 6, 2])
    assert not Solution().increasingTriplet([4, 8, 4, 1, 7])
    assert Solution().increasingTriplet([4, 4, 5, 8, 6])

    # Longer sequences
    assert Solution().increasingTriplet([1, 2, 3, 4, 5])
    assert not Solution().increasingTriplet([5, 4, 3, 2, 1])
    assert Solution().increasingTriplet([2, 1, 5, 0, 4, 6])  # one solution is 1 5 6
    assert Solution().increasingTriplet(
        [2, 1, 9, 0, 4, 6]
    )  # remove that solution - only 0 4 6
    assert Solution().increasingTriplet([2, 1, 9, 5, 4, 6])  # solution is 1 4 6
    assert not Solution().increasingTriplet([10, 6, 10, 6, 2, 5, 0, 3])
    assert not Solution().increasingTriplet([0, 9, 9, 0, 9, 9, 0, 7])
    assert not Solution().increasingTriplet([7, 5, 9, 9, 5, 9, 7, 2])
    assert Solution().increasingTriplet([7, 9, 1, 1, 3, 9, 0, 9])
    assert Solution().increasingTriplet([10, 9, 10, 2, 1, 2, 5, 10])

    # Test longer sequence with duplicated arrays
    assert Solution().increasingTriplet(
        [2, 2, 2, 0, 4, 6]
    )  # try with duplicated numbers
    assert Solution().increasingTriplet([0, 1, 0, 0, 4, 6])
    assert not Solution().increasingTriplet([2, 2, 2, 0, 2, 1])
