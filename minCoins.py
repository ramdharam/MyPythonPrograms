def minCoins(v):
    arr =[1000, 500, 200, 100, 50, 20, 10, 5, 1]
    count, i = 0, 0
    if v == 0:
        return 0
    while v > 0:
        while i < len(arr):
            if v ==0:
                return count
            if v >= arr[i] and i==0:
                count = count + v/arr[i]
                v = v%arr[i]

            if v >= arr[i] and v < arr[i-1] and i != (len(arr)-1):
                count = count + v/arr[i]
                v = v%arr[i]

            if i == len(arr)-1 and arr[i]==1:
                count = count + v/arr[i]
                v = v - (v/arr[i])

            i +=1
    return count


print (minCoins(9999))