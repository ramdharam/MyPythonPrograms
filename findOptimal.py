def findOptimal(n):
    """
    :param n:
    :return:
    """
    res = list()
    ## values <7 will have n as the optimal value
    for i in xrange(7):
        res.append(i+1);
    i = 0
    for i in xrange(7,n+1):
        res[i-1] = 0
        for j in xrange(i-3, 0, -1):
            curr = (i-j-1) * res[j-1]
            if curr > res[i-1]:
                res[i-1] = curr
    return res[n-1]


print(findOptimal(7))