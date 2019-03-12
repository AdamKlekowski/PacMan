class Graph(object):
    def __init__(self):
        self.vertex=[]
        self.edge=[]
        self.path=[]

    def checkIndexVertex(self, coordinatesVertex):
        index=0
        for vertex in self.vertex:
            if vertex==coordinatesVertex:
                return index
            index+=1
        return -1

    def completeEdge(self):
        for vertex in self.vertex:
            tmp=[]
            x=vertex[0]
            y=vertex[1]
            if self.checkIndexVertex((x-1,y)) != -1:
                tmp.append(self.checkIndexVertex((x-1,y)))
            if self.checkIndexVertex((x+1,y)) != -1:
                tmp.append(self.checkIndexVertex((x+1,y)))
            if self.checkIndexVertex((x,y-1)) != -1:
                tmp.append(self.checkIndexVertex((x,y-1)))
            if self.checkIndexVertex((x,y+1)) != -1:
                tmp.append(self.checkIndexVertex((x,y+1)))

            self.edge.append(tmp)

    def completeVertex(self, game):
        y=0
        for line in game.map:
            x=0
            for char in line:
                if char=="f" or char=="p" or char=="e":
                    self.vertex.append((x,y))
                x+=1
            y+=1
        self.completeEdge()

    #BFS
    def shortestPath(self, pacmanPosition, enemyPosition):
        self.path=[]
        queue=[]
        previous=[-1 for _ in range(len(self.vertex))]
        visitedVertex=[]
        queue.append(self.checkIndexVertex(enemyPosition))

        while len(queue)!=0:
            for element in self.edge[queue[0]]:
                if ((element in visitedVertex) == False):
                    previous[element]=queue[0]
                    queue.append(element)
                if self.vertex[element]==pacmanPosition:
                    while element!=-1:
                        self.path.append(previous[element])
                        element=previous[element]
                    self.path.pop()
                    if len(self.path)>0:
                        self.path.pop()
                        self.path.reverse()
                    self.path.append(self.checkIndexVertex(pacmanPosition))
                    return
            visitedVertex.append(queue[0])
            queue.pop(0)