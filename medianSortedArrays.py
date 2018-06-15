def median(a, b):
    arrLen = len(a) + len(b)
    if arrLen%2 == 0:
        midIdx = arrLen/2
    else:
        midIdx = arrLen/2
    i , j = 0, 0
    idx = 0
    c=[]
    while idx <= midIdx:
        if  i < len(a) and j< len(b) and a[i] < b[j]:
            c.append(a[i])
            i +=1
            idx +=1

        elif i < len(a) and j < len(b) and b[j] < a[i]:
            c.append(b[j])
            j +=1
            idx +=1
        elif i < len(a) and j < len(b) and a[i] == a[j]:
            c.append(a[i])
            c.append(b[j])
            i +=1
            j +=1
            idx +=2
        else:
            if i >= len(a):
                c.append(b[j])
                j +=1
                idx +=1
            elif j >= len(b):
                c.append(a[i])
                i +=1
                idx +=1

    if arrLen%2 == 0:
        return round((c[midIdx] + c[midIdx-1]) / 2.0, 2)
    else:
        return round(c[midIdx])




a=[1,2,3,4]
b=[5,6,7,8]
print( median(a,b) )