def rabinKarp(text, pattern, d, q):
    """

    :param text:
    :param pattern:
    :param d:  number of alphabets
    :param q:  a prime number
    :return:
    """
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1)%q
    p, t = 0,0
    results =[]
    for i in xrange(m):
        p = (d*p + ord(pattern[i]))%q
        t = (d*t + ord(text[i]))%q
    for j in xrange(n-m+1):
        if p == t:
            match = True
            for k in xrange(m):
                if pattern[k] != text[k+j]:
                    match = False
                    break
            if match:
                results = results + [j]
        if j < n-m:
            t = (t-h*ord(text[j]))%q
            t = (d*t + ord(text[j+m]))%q
            t = (t+q)%q
    return results

print(rabinKarp("asdsdfgdgd", "sdf", 256, 11))
