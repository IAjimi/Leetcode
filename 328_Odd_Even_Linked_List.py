# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        """
        Runtime: 40 ms, faster than 85.28% of Python3 online submissions.
        Memory Usage: 16.3 MB, less than 55.22% of Python3 online submissions.
        """
        if not head:
            return head
        elif not head.next:
            return head
        elif not head.next.next:
            return head
        else:
            dummy = head
            odd, even, head = head, head.next, head.next.next

            while even.next:
                odd.next, head.next, even.next = head, odd.next, head.next
                if even.next and even.next.next:
                    odd, even, head = head, even.next, even.next.next
                else:
                    break

        return dummy
