class Solution:
	def shiftingLetters(self, s: str, shifts: List[int]) -> str:
		"""
		Runtime: 1018 ms, faster than 22.22% of Python3 online submissions.
		Memory Usage: 25.1 MB, less than 63.67% of Python3 online submissions.
		"""
		# Convert s to ordinal numbers, indexed at 0 for a (note: ord('a') = 97)
		s = [ord(c) - 97 for c in s]

		# Simply shifts so shift[i] has total shifts for letter i
		for i in range(len(shifts) - 1, -1, -1):
			if i == len(shifts) - 1:
				shifts[i] = shifts[i] % 26
			else:
				shifts[i] = (shifts[i] + shifts[i + 1]) % 26

		# Translate shifts back to string
		s = [(c + shift) % 26 for c, shift in zip(s, shifts)]
		s = [chr(c + 97) for c in s]
		return ''.join(s)
