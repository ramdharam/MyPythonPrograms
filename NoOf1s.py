def numberOf1s(i):
    count=0
    while i > 0:
        if i%2!=0:
            count+=1
        i=i/2
    print(count)

numberOf1s(3)