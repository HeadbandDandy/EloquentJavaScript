class Solution:
    def isSubsequence(self, s: str, t: str):
        # two pointers placed
        i = j = 0
        # loop runs until one of pointers gets to end of its string
        while i < len(s) and j < len(t):
            # each iteration checks character
            # each string must be exhausted
            # each iteration through array returns matching characters
            # until characters are gone
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)