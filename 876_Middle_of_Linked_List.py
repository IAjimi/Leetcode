# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Runtime: 36 ms, faster than 58.14% of Python3 online submissions for Middle of the Linked List.
        Memory Usage: 13.8 MB, less than 83.82% of Python3 online submissions for Middle of the Linked List.
        """
        n = 1
        node = head

        while node.next:
            node = node.next
            n += 1

        midpoint = n // 2
        node = head
        for _ in range(midpoint):
            node = node.next

        return node
