# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		"""
		Runtime: 32 ms, faster than 92.14% of Python3 online submissions.
		Memory Usage: 14.3 MB, less than 59.55% of Python3 online submissions.
		"""
		if k == 0 or not head:
			return head
		elif not head.next:
			return head
		else:
			# Get to tail, get length of list
			n = 1
			tail = head

			while tail.next:
				tail = tail.next
				n += 1

			# Get updated k
			k = k % n

			if k == 0:
				return head

			# Add pointer from tail to head
			tail.next = head

			# Move n - k - 1 right from head, create tail, update head
			counter = 0
			tail = head

			while counter < n - k - 1:
				tail = tail.next
				counter += 1

			head, tail.next = tail.next, None

			return head


