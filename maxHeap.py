class maxHeap(object):
    def __init__(self):
        self.l=[0]
        self.currSize =0

    def add(self, n):
        self.l.append(n)
        self.currSize +=1
        self.__bubbleUp__()

    def __bubbleUp__(self):
        i = self.currSize
        while i//2>0:
            if self.l[i] > self.l[i//2]:
                tmp = self.l[i//2]
                self.l[i//2] = self.l[i]
                self.l[i] = tmp
            i = i//2

    def peek(self):
        return self.l[1]


    def swap(self, i, j):
        tmp = self.l[i]
        self.l[i] = self.l[j]
        self.l[j] = tmp

    def __bubbleDown__(self):
        i = 1
        while (i*2 < self.currSize or i*2+1 < self.currSize) \
                and (self.l[i] < self.l[i*2] or self.l[i] < self.l[i*2 + 1]):
            if self.l[i*2] < self.l[i*2 +1]:
                self.swap(i, i*2+1)
                i = i*2 +1
            elif self.l[i*2] > self.l[i*2 +1]:
                self.swap(i, i*2)
                i = i*2
            elif self.l[i*2] == self.l[i*2 +1]:
                self.swap(i, i*2)
                i = i*2


    def poll(self):
        tmp = self.l[1]
        self.l[1] = self.l.pop()
        self.currSize -=1
        self.__bubbleDown__()
        return tmp




if __name__ == "__main__":
    mh = maxHeap()
    mh.add(2)
    mh.add(5)
    print(mh.peek())
    mh.add(3)
    mh.add(7)
    print(mh.peek())
    print(mh.l)
    print(mh.poll())
    print(mh.l)
    print(mh.peek())




