import heapq as hq

def heapSort(arr):
    for i in xrange(len(arr)):
        hq.heapify(arr[i:])
        arr = list(arr)
    print arr

a=[11,2,4, 7, 6]
heapSort(a)