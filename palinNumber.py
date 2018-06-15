def palinNumber(n):
    p=n
    q=0
    if p <0:
        return False
    while(p>q):
        q = (q*10) + p%10
        p = p/10
    return True if (p==q or p == q/10) else False

print(palinNumber(12421))