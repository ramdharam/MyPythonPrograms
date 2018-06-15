import sys

def reverseInt(n):
    s = cmp(n,0)
    r = int(`s*n`[::-1])
    return (s*r) if (r < 2**31) else 0


print (sys.maxint)
print(reverseInt(2147483647))