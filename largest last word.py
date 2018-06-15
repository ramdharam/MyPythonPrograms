class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        if len(A) == 0:
            return 0
        wordstart, wordend = 0,0
        isStart = False
        for i in xrange(len(A)):
            if wordstart == 0 and wordend==0 and isStart == False and A[i] != ' ':
                wordstart = i
                isStart = True
            elif isStart == True and A[i] == ' ':
                wordend = i-1
                isStart = False
            elif isStart == False and A[i] != ' ':
                wordstart = i
                isStart = True
        if isStart == True:
            wordend = i
        print (wordend, wordstart)
        out = (wordend - wordstart) +1
        if out > 0:
            return out
        else:
            return 0

a = Solution()
print(a.lengthOfLastWord("Hello World   "))