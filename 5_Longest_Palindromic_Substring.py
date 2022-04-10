class Solution:
    def check_palindrome(self, string: str) -> bool:
        if string == string[::-1]:
            return True
        else:
            return False

    def longestPalindrome(self, string: str) -> str:
        """
        Runtime: 3796 ms, faster than 29.86% of Python3 online submissions.
        Memory Usage: 14.4 MB, less than 62.80% of Python3 online submissions.
        """
        max_palindrome = ""
        positions = {}

        for ix in range(len(string)):
            s = string[ix]

            if s in positions:
                prev_ix = positions[s]
                for pix in prev_ix:
                    palindrome = string[pix : ix + 1]
                    is_palindrome = self.check_palindrome(palindrome)
                    if is_palindrome and len(palindrome) > len(max_palindrome):
                        max_palindrome = palindrome

                positions[s].append(ix)
            else:
                positions[s] = [ix]

        if max_palindrome == "":
            return string[0]
        else:
            return max_palindrome
