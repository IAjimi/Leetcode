from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getNum(self, l1: ListNode) -> int:
        """
        Returns the number represented by a Linked List.

        Example:
        > self.getNum([1,2,3,0])
        # 321
        """
        l1_num = ""
        while l1:
            l1_num += str(l1.val)
            l1 = l1.next

        return int(l1_num[::-1])

    def manyPassAddTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Runtime: 72 ms, faster than 57.08% of Python3 online submissions.
        Memory Usage: 14.2 MB, less than 90.14% of Python3 online submissions.
        """
        l1_num = self.getNum(l1)
        l2_num = self.getNum(l2)
        target = str(l1_num + l2_num)[::-1]

        dummy = l1

        for ix in range(len(target)):
            l1.val = int(target[ix])
            if not l1.next and ix < len(target) - 1:
                l1.next = ListNode()
            l1 = l1.next

        return dummy

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Note: there is a more concise way to handle the if/else loop but it adds 20ms to the runtime.

        Runtime: 76 ms, faster than 63.13% of Python3 online submissions for Add Two Numbers.
        Memory Usage: 13.9 MB, less than 98.33% of Python3 online submissions for Add Two Numbers.
        """
        node1 = l1
        node2 = l2
        carry_over = 0
        l3 = []

        while node1 or node2 or carry_over > 0:
            node1 = node1 if node1 else ListNode(0)
            node2 = node2 if node2 else ListNode(0)

            new_val = node1.val + node2.val + carry_over

            if new_val < 10:
                l3.append(ListNode(new_val))
                carry_over = 0
            else:
                l3.append(ListNode(new_val - 10))
                carry_over = 1

            node1 = node1.next
            node2 = node2.next

        for ix in range(len(l3) - 1):
            l3[ix].next = l3[ix + 1]

        return l3[0]
