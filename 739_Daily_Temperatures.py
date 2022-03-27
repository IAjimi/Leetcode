from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Runtime: 1552 ms, faster than 50.11% of Python3 online submissions for Daily Temperatures.
        Memory Usage: 24.1 MB, less than 97.81% of Python3 online submissions for Daily Temperatures.

        Add to queue when the last element in the queue is > current element.
        Otherwise, remove all elements (right to left) in queue that are < than current element.
        Update removed element's value in answer array.

        Example:
            # 0   1   2   3   4   5   6   7
            # 73, 74, 75, 71, 69, 72, 76, 73
            #  .                                []
            #      .                            [(0,73)]
            #          .                        [(1,74)]
            #              .                    [(2, 75)]
            #                  .                [(2, 75), (3, 71)] <- 71 is smaller, so we add it to queue
            #                      .            [(2, 75), (3, 71), (4, 69)]
            #                          .        [(2, 75)] <- 72 was larger than some elements, so we clear part of queue
            #                              .    [(6, 76)]
            #  we are left with [(6, 76), (7,73)]
        """
        queue = []
        answer = [0 for n in temperatures]

        for i, v in enumerate(temperatures):
            while queue and v > queue[-1][1]:  # smallest element at back
                j, _ = queue.pop()
                answer[j] = i - j

            queue.append((i, v))

        return answer
