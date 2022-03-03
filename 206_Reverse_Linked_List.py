from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach.

        Runtime: 32 ms, faster than 93.94% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 15.4 MB, less than 85.09% of Python3 online submissions for Reverse Linked List.
        """
        left = None
        right = head

        while right:
            temp = right.next
            right.next = left

            left = right
            right = temp

        return left  # last iteration, right is None

    def recursiveReverseList(
        self, head: Optional[ListNode], previous: Optional[ListNode] = None
    ) -> Optional[ListNode]:
        """
        Recursive approach.

        Runtime: 39 ms, faster than 69.48% of Python3 online submissions for Reverse Linked List.
        Memory Usage: 20.4 MB, less than 7.57% of Python3 online submissions for Reverse Linked List.
        """
        if not head:
            return head

        if head.next:
            old_next_node = head.next
            head.next = previous

            next_node = self.reverseList(old_next_node, head)
            return next_node

        head.next = previous
        return head
