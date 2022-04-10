# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Runtime: 89 ms, faster than 59.01% of Python3 online submissions for Remove Linked List Elements.
        Memory Usage: 17.8 MB, less than 56.90% of Python3 online submissions for Remove Linked List Elements.
        """
        # find new head if head has val
        while head and head.val == val:
            head = head.next

        # empty list
        if not head:
            return None

        # iterate thru list to remove val
        left = head
        right = head.next

        while left and right:
            # find 1st right-side element without val
            while right and right.val == val:
                right = right.next

            left.next = right
            left = left.next if left.next else None
            right = right.next if right and right.next else None

        return head
