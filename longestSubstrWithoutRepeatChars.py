def longSubstr(n):
    if len(n)==0:
        return ''
    maxLen = 0
    start = 0
    mydict = {}
    l = len(n)
    for i in xrange(l):
        if n[i] in mydict and start <= mydict[n[i]]:
            start = mydict[n[i]] + 1
        else:
            maxLen = max(maxLen, i - start +1)
        mydict[n[i]] = i
    return  maxLen


a="dvdf"
print(longSubstr(a))