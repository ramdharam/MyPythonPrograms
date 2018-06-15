def getTotalX(a, b):
    count = 0
    l1 = len(a)
    l2 = len(b)
    if l1 == 0 or l2 == 0:
        return 0
    for i in xrange(a[l1-1],b[0]+1):
        breaker = False
        for j in a:
            if i%j != 0:
                breaker = True
                break
        if breaker:
            continue
        for k in b:
            if k%i != 0:
                breaker = True
                break
        if breaker:
            continue
        count +=1
    return count

a = [2,4]
b = [16, 32, 96]
total = getTotalX(a, b)
print(total)