from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 65 ms, faster than 37.86% of Python3 online submissions for Remove Duplicates from Sorted List II.
        Memory Usage: 13.8 MB, less than 85.61% of Python3 online submissions for Remove Duplicates from Sorted List II.
        """
        # move head forward
        duplicates = set()
        while head and (
            head.val in duplicates or (head.next and head.val == head.next.val)
        ):
            duplicates.add(head.val)
            head = head.next

        left = head
        right = head.next if head else None

        while left and right:
            while right and (
                right.val in duplicates or (right.next and right.val == right.next.val)
            ):
                duplicates.add(right.val)
                right = right.next

            left.next = right
            left = left.next if left else None
            right = right.next if right else None

        return head
