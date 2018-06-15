class queueNode:
    def __init__(self, v=0, dist =0):
        self.v = v
        self.dist = dist

def snakeAndLadderMinDice(move, N):
    visited = [False] * N
    queue = []
    visited[0] = True
    queue.append(queueNode(0,0))
    qe = queueNode()
    while queue:
        qe = queue.pop(0)
        v = qe.v
        if v == N-1:
            break
        j = v + 1
        while j <= v+6 and j<N:
            if visited[j] is False:
                a=queueNode()
                a.dist = qe.dist + 1
                visited[j] = True

                a.v = move[j] if move[j] != -1 else j
                queue.append(a)
        j +=1
    return qe.dist
