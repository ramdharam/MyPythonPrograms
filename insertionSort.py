def insertionSort(a):
    for i in xrange(len(a)-1):
        j=i+1
        temp = a[j]
        while (j>0) and temp < a[j-1]:
            a[j] =a[j-1]
            j -=1
        a[j] = temp
    print(a)

a=[5,3,2,6,4, 21, 3, 1, 0]
insertionSort(a)


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    result = []
    i = j = 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j +=1

        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break

    return result

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    middle = len(arr)/2
    left = mergeSort(arr[:middle])
    right = mergeSort(arr[middle:])

    return merge(left, right)

a=[5,3,2,6,4, 21, 3, 1, 0]
print(mergeSort(a))