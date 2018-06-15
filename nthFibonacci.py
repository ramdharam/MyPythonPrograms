class Solution():
    def nthFibonacci(self, n):
        if n == 0 or n ==1:
            return 1
        sol = [None for _ in xrange(n+1)]
        sol[0] = 0
        sol[1] = 1
        i = 2
        while i <= n:
            sol[i] = sol[i-1] + sol[i-2]
            i +=1
        return sol[n]

a= Solution()
print(a.nthFibonacci(10))