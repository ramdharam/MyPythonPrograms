def strstr(str, substr):
    if str is None or substr is None:
        return -1
    l = len(substr)
    s = len(str)
    if l > str:
        return -1
    for i in xrange(s-l + 1):
        if str[i:i+l] == substr:
            return i
    return -1


print(strstr('GeeksForGeeks', 'For'))