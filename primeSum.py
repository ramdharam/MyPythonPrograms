class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A == 0:
            return 0
        primes = [1] * (A+1)
        primes[0] = 0
        primes[1] = 0
        for i in xrange(4,A+1,2):
            primes[i] = 0
        for i in xrange(3,int(A**0.5)+1,2):
            if primes[i]==1:
                k=2
                j=i*k
                while j <= A:
                    primes[j] = 0
                    k+=1
        print primes
        return [1,1]

A = Solution()
print(A.primesum(10))