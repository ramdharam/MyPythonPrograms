def pairs(a, k):
    # a contains array of numbers and k is the value of difference
    answer = 0
    a.sort()
    s = len(a)
    i = 0
    while i < s and a[i] + k <= a[s - 1]:

        l = i + 1
        r = s - 1
        match = False
        val = a[i] + k
        while (l <= r):
            mid = (l + r) / 2
            if a[mid] == val:
                match = True
                answer += 1
                break
            elif a[mid] < val:
                l += 1
            elif a[mid] > val:
                r -= 1
        i += 1
    return answer


a = [1,5,3,4,2]
print(pairs(a, 2))