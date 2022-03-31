from typing import List


class Solution:
    def naiveCorpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """Time Limit Exceeded.
        Time: O(n x m), where m is the size of bookings.
        Space: O(n)
        """
        answer = []

        for flight in range(n):
            count = 0

            for first, last, seats in bookings:
                if first - 1 <= flight <= last - 1:
                    count += seats

            answer.append(count)

        return answer

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        """
        Runtime: 1472 ms, faster than 17.64% of Python3 online submissions for Corporate Flight Bookings.
        Memory Usage: 27.9 MB, less than 91.56% of Python3 online submissions for Corporate Flight Bookings.

        Example:
        ix: [ 0,  1,   2,  3, 4,  5]    bookings
            [ 0,  0,   0,  0, 0,  0]    --------
            [10,  0, -10,  0, 0,  0]     1,2,10
            [10, 20, -10,-20, 0,  0]     2,3,20
            [10, 45, -10,-20, 0,-25]     2,5,25
        ->  [10, 55, 45, 25, 25]
        """
        answer = [0 for _ in range(n + 1)]  # one extra space for last = n.

        for first, last, seats in bookings:
            answer[first - 1] += seats
            answer[last] -= seats

        for i, val in enumerate(answer):
            if i > 0:
                answer[i] += answer[i - 1]

        return answer[:-1]
