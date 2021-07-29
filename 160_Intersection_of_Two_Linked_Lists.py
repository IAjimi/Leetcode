# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def createStack(self, headA: ListNode) -> List[ListNode]:
		stack = []

		while headA:
			stack.append(headA)
			headA = headA.next

		return stack

	def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
		"""
		Runtime: 152 ms, faster than 95.51% of Python3 online submissions.
		Memory Usage: 29.5 MB, less than 53.96% of Python3 online submissions.
		"""
		if headA and headB:
			stackA = self.createStack(headA)
			stackB = self.createStack(headB)
			intersect = 0

			while stackA and stackB:
				topA = stackA.pop()
				topB = stackB.pop()
				if topA != topB:
					if intersect == 0:
						return None
					else:
						return prev
				else:
					intersect += 1
					prev = topA

			return prev
		else:
			return None

