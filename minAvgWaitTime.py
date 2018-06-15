class CustomMinHeap:
    def __init__(self):
        self.ls = []

    def push(self, val):
        self.ls.append(val)

    def pop(self):
        self.ls.pop(0)

    def heapify(self):
