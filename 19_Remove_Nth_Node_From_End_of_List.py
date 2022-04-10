from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        # 1. get the number of nodes in list
        node = head
        length = 0

        while node:
            node = node.next
            length += 1

        # special case: removing head
        if n == length:
            return head.next

        # 2. get to nth node
        target = length - n - 1

        left = head
        right = head.next

        for i in range(target):
            left = left.next
            right = right.next

        # remove nth node
        right = right.next
        left.next = right

        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # special case: only 1 input
        # 10:38

        # 1 2 3 4 5 6 7 8
        #         4 3 2 1 <- n = 4
        # r
        # . . . r
        # l     r
        #   l     r
        #     l     r
        #       l     r
        #         l     r  <- hit the end

        # handle singleton
        if not head.next:
            return None

        # otherwise...
        left = head
        right = head

        for _ in range(n):
            right = right.next

        # move until hit target
        while right.next:
            left = left.next
            right = right.next

        # remove target
        left.next = right

        return head
