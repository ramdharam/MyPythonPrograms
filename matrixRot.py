a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print (a)

def transpose(a):
    for i in xrange(len(a)):
        for j in xrange(i, len(a[0])):
            temp = a[i][j]
            a[i][j]= a[j][i]
            a[j][i] = temp
    print (a)

def revCols(a):
    for i in xrange(len(a)):
        j =0
        k = len(a[i])-1
        while (j < k):
            temp=a[j][i]
            a[j][i]=a[k][i]
            a[k][i] = temp
            j+=1
            k-=1
    print (a)

def revRows(a):
    for i in xrange(len(a)):
        j=0
        k=len(a[i])-1
        while (j < k):
            temp = a[i][k]
            a[i][k] = a[i][j]
            a[i][j]=temp
            j +=1
            k -=1
    print(a)


transpose(a)
#revCols(a)
revRows(a)
