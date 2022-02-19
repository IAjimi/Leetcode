from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 46 ms, faster than 41.77% of Python3 online submissions for Swap Nodes in Pairs.
        Memory Usage: 14 MB, less than 75.41% of Python3 online submissions for Swap Nodes in Pairs.

        Example:
            >   1 2 3 4
            # L M R
            >   2 1 3 4
            # L R M
            >   2 1 3 4
            #   L R M
            >   2 1 4 3
            #   L M R
            >   2 1 4 3
            #       L M R
        """

        if not head:
            return None
        elif not head.next:
            return head

        left = None
        mid = head
        head = right = mid.next

        while mid and right:
            mid.next, right.next = right.next, mid

            if left:
                left.next = right

            if mid.next and mid.next.next:
                left = mid
                mid = mid.next
                right = mid.next
            else:
                break

        return head
