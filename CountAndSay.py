def CountAndSay(n):
    """
    Count and say the sequence
    :param n:
    :return:
    """
    if n==0:
        return "0"
    if n==1:
        return "1"
    if n==2:
        return "11"
    st = "11"
    for i in xrange(3,n+1):
        st +='$'
        l = len(st)
        cnt = 1
        t = ''
        for j in xrange(1, l):
            if st[j] != st[j-1]:
                t += str(cnt) + st[j-1]
                cnt =1
            else:
                cnt +=1
        st = t
    return st

n =4
print(CountAndSay(n))
