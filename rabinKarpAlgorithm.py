def RabinKarpSearch(pattern, text, q, d):
    """

    :param pattern:
    :param text:
    :param q:  a prime numbers
    :return:
    """
    n = len(text)
    m = len(pattern)
    h = pow(d, m-1)%q
    p = 0
    t = 0
    result = []
    for i in xrange(m):
        p = (d*p + ord(pattern[i]))%q
        t = (d*t + ord(text[i]))%q
    for j in xrange(n-m+1):
        if p == t:
            match = True
            for i in xrange(m):
                if pattern[i] != text[j+i]:
                    match = False
                    break
            if match:
                result = result + [j]
        if j < n-m:
            t = (t-h*ord(text[j]))%q
            t = (t*d + ord(text[j+m]))%q
            t = (t+q)%q
    return result


print(RabinKarpSearch("sdf","asdsdfgdfggd",11, 256))


