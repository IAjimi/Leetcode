class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        """
        Runtime: 195 ms, faster than 33.65% of Python3 online submissions for Find the Winner of the Circular Game.
        Memory Usage: 13.8 MB, less than 80.36% of Python3 online submissions for Find the Winner of the Circular Game.
        """
        # create linked list data structure
        linked_list = {i: [i - 1, i + 1] for i in range(1, n + 1)}
        linked_list[1] = [n, 2]
        linked_list[n] = [n - 1, 1]

        # run simulation
        eliminated_pos = 1
        remaining = n

        while remaining > 1:
            # get to next eliminated node
            for j in range(k - 1):
                eliminated_pos = linked_list[eliminated_pos][1]

            # update pointers in linked list
            prev_pos, next_pos = linked_list[eliminated_pos]
            linked_list[prev_pos][1] = next_pos
            linked_list[next_pos][0] = prev_pos

            # remove eliminated node
            del linked_list[eliminated_pos]

            # move on
            eliminated_pos = next_pos
            remaining -= 1

        return list(linked_list.keys())[0]
