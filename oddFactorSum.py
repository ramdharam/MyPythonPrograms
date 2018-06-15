def oddFactorSum(n):
    if n==0:
        return 0
    if n==1:
        return 1
    s =0
    for i in xrange(1, (n/2)+1, 2):
        if n%i == 0:
            s = s+i
    return s

print(oddFactorSum(30))
