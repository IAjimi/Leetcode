class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
        Top 20% by speed.
        '''
        palindrome = [l.lower() for l in s if l.isalpha() or l.isdigit()]
        if palindrome == palindrome[::-1]:
            return True
        else:
            return False