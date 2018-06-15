def commonElem3Str(ar1, ar2, ar3):
    l1 = len(ar1)
    l2 = len(ar2)
    l3 = len(ar3)

    out = []
    i,j,k = 0,0,0

    while i< l1 and j< l2 and k< l3:
        if ar1[i]==ar2[j] and ar2[j]==ar3[k]:
            out.append(ar1[i])
            i +=1
            j +=1
            k +=1
        elif ar1[i] < ar2[j]:
            i +=1
        elif ar2[j] < ar3[k]:
            j +=1
        else:
            k +=1

    return  out


a = [1,2,3,4,5]
b = [3,4,5,6]
c = [3,4,5, 12, 13]

print(commonElem3Str(a,b,c))
