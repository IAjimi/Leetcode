class Solution:
	def isValid(self, string: str) -> bool:
		"""
		Runtime: 28 ms, faster than 86.17% of Python3 online submissions.
		Memory Usage: 14.3 MB, less than 63.45% of Python3 online submissions.
		"""
		stack = []
		matches = {
			')': '(',
			'}': '{',
			']': '['
		}

		for char in string:
			if char in ['(', '[', '{']:
				stack.append(char)
			elif char in [')', ']', '}']:
				if stack:
					matching_char = stack.pop()

					if matching_char != matches[char]:
						return False
				else:  # unmatched closed bracket
					return False

		if stack:  # if stack isn't empty, some characters weren't match
			return False
		else:
			return True