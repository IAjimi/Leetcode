from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Runtime: 84 ms, faster than 37.35% of Python3 online submissions for Linked List Cycle.
        Memory Usage: 18 MB, less than 15.68% of Python3 online submissions for Linked List Cycle.
        """
        visited = set()

        node = head

        while node:
            if node in visited:
                return True

            visited.add(node)
            node = node.next

        return False

    def pointerHasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Two pointers, one "slow" (moves by one per turn), other "fast" (moves by two per turn),
        so they converge when there is a cycle.

        Runtime: 71 ms, faster than 62.32% of Python3 online submissions for Linked List Cycle.
        Memory Usage: 17.6 MB, less than 74.54% of Python3 online submissions for Linked List Cycle.
        """
        if not head:
            return False

        fast = head.next.next if head.next and head.next.next else None
        slow = head.next if head.next else None

        while fast != slow:
            fast = fast.next.next if fast and fast.next and fast.next.next else None
            slow = slow.next if slow and slow.next else None

        return not (slow is None and fast is None)
