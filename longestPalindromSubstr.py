class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s is None:
            return ''
        l = len(s)
        sol = [[None for _ in xrange(l)] for _ in xrange(l)]
        # len of 1
        for i in xrange(l):
            sol[i][i] = True
            start, end = i, i
            # len of 2
        for i in xrange(l - 1):
            if s[i] == s[i + 1]:
                sol[i][i + 1] = True
                start, end = i, i + 1

        # len > 3:
        for wl in xrange(3, l + 1):
            for i in xrange(l - wl + 1):
                j = i + wl - 1
                if s[i] == s[j] and sol[i + 1][j - 1] == True:
                    sol[i][j] = True
                    start, end = i, j
        # print (start, end)
        return s[start:end + 1]

obj = Solution()
print(obj.longestPalindrome('abcba'))