# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def isPalindrome(self, head: ListNode) -> bool:
		"""
		Runtime: 816 ms, faster than 60.45% of Python3 online submissions.
		Memory Usage: 47.1 MB, less than 49.47% of Python3 online submissions.
		"""
		palindrome = []

		while head:
			palindrome.append(head.val)
			head = head.next

		if palindrome[::-1] == palindrome:
			return True
		else:
			return False
