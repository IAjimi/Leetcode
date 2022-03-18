class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        """
        Runtime: 32 ms, faster than 86.28% of Python3 online submissions for Score of Parentheses.
        Memory Usage: 13.9 MB, less than 30.17% of Python3 online submissions for Score of Parentheses.

        Example:
            0 1 2 3 4 5 6 7 8 9 10 11
            ( ( ( ( ) ) ( ( ) ) ) )     stack       score
                  i                    [0,1,2,3]
                  j i                  [0,1,2]     [(4,1)]
                j     i                [0,1]       [(5,2)]
                          i            [0,1,6,7]   [(5,2)]
                          j i          [0,1,6]     [(5,2),(8,1)]
                        j     i        [0,1]       [(5,2),(9,2)]
              j                 i      [0]         [(10,8)]
            j                      i   []          [(11,16)]
        """
        score = []
        stack = []

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            else:
                # get index of matching parenthesis
                j = stack.pop()

                # get score of items btw the ) and (
                cur_score = 0

                while score and score[-1][0] > j:
                    cur_score += score[-1][1]
                    score.pop()

                if i == j + 1:
                    cur_score += 1
                else:
                    cur_score *= 2

                # update score
                score.append((i, cur_score))

        return sum([s for i, s in score])
