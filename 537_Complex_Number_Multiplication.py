class Solution:
	def stringToNum(self, num1: str):
		"""
		Takes a complex number formatted as a string and returns the
		real and imaginary values of the complex number separately.

		Example:
			> self.stringToNum(num1="3+-1i")
			# 3, -1
		"""
		real, imaginary = num1.split('+')  # 1, -1i
		imaginary = imaginary.replace('i', '')
		return int(real), int(imaginary)

	def complexNumberMultiply(self, num1: str, num2: str) -> str:
		"""
		Runtime: 24 ms, faster than 92.57% of Python3 online submissions.
		Memory Usage: 14.1 MB, less than 89.22% of Python3 online submissions.

		Returns the product of two complex numbers.

		Uses simple arithmetic:
			> (a + bi) * (c + di)
			> a * c + (a * d + b * c)*i + (b * d)i**2
			> (a * c - b * d) + (a * d + b * c)*i
		"""
		a, b = self.stringToNum(num1)
		c, d = self.stringToNum(num2)

		real = a * c - b * d
		imaginary = a * d + b * c

		return f"{real}+{imaginary}i"