# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def getNum(self, l1: ListNode) -> int:
		'''
		Returns the number represented by a Linked List.

		Example:
		> self.getNum([1,2,3,0])
		# 321
		'''
		l1_num = ''
		while l1:
			l1_num += str(l1.val)
			l1 = l1.next

		return int(l1_num[::-1])

	def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
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
