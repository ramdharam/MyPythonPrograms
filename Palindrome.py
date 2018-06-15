class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        l,r = 0, len(s)-1
        #print(len(s))
        #print (s[0], s[1])
        while r -l >= 1:
            while r-l >=1 and l < len(s) and not s[l].isalnum():
                l +=1
            while r-l >=1 and r >=0 and not s[r].isalnum() :
                r -=1
            if s[l] != s[r]:
                return False
            l +=1
            r -=1
        return True


s = Solution()
out = s.isPalindrome("  ")
print out