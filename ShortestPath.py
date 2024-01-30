import tkinter as tk
import copy

window = tk.Tk()
canvas = tk.Canvas(window, width=800, height=600, bg="#ffffff")
canvas.pack()

def inputTitik(n):
    setOfVertex = []
    for noUrut in range(n):
        titik = input()
        x = int(titik.split(' ')[0])
        y = int(titik.split(' ')[1])
        canvas.create_oval(x-10, y+10, x+10, y-10, fill='blue')
        canvas.create_text(x, y-15, text=noUrut, font=7)
        setOfVertex.append([x, y])

    return setOfVertex

def inputStartTarget(vertices):
    target = input()
    start = int(target.split(' ')[0])
    end = int(target.split(' ')[1])

    return[vertices[start], vertices[end]]

def ConnectEdge(Vertices):
    edges = []
    n = int(input())
    for x in range(n):
        edgeInput = input()
        v1 = int(edgeInput.split(' ')[0])
        v2 = int(edgeInput.split(' ')[1])
        weight = int(edgeInput.split(' ')[2])

        edges.append([Vertices[v1], Vertices[v2], weight])
        canvas.create_line(Vertices[1], Vertices[2])
        canvas.create_text((Vertices[v1][0] + Vertices[v2][0]) / 2 , (Vertices[v1][1] + Vertices[v2][1]) / 2, text=weight, font=7) 

    return edges

def findNeighbor(edges, CurrentPosition, visitedVertex):
    commonNeighbor = []
    setOfEdge = copy.deepcopy(edges)
    visited = copy.deepcopy(visitedVertex)
    for edge in setOfEdge:
        if (CurrentPosition == edge[0] or CurrentPosition == edge[1]):
            edge.remove(CurrentPosition)
            if edge[0] not in visited:
                commonNeighbor.append(edge[0])
    return commonNeighbor

def SumColumn(list2d, extractedColumn):
    value = []
    for edge in list2d:
        value.append(edge[extractedColumn])
    return sum(value)

def findShortestPath(setOfPath):
    eachPath = []
    for x in setOfPath:
        eachPath.append(SumColumn(x, 2))
    minPath = min(eachPath)

    return setOfPath[eachPath.index(minPath)]

def Path(edges, CurrentPosition, TargetVertex, walk=[], VisitedVertex=[]):
    NeighborVertex = findNeighbor(edges, CurrentPosition, VisitedVertex)
    if len(NeighborVertex) == 0:
        return None
    
    for neighbor in NeighborVertex:
        if neighbor[0] == TargetVertex:
            walk.append([CurrentPosition, neighbor[0], neighbor[1]])
            path.append(copy.deepcopy(walk))
            walk.pop()
            return None
        
        else: 
            VisitedVertex.append(CurrentPosition)
            walk.append([CurrentPosition, neighbor[0], neighbor[1]])

            Path(edges, neighbor[0], TargetVertex, walk, VisitedVertex)
            VisitedVertex.pop()
            walk.pop()

nVertex = int(input())
vertices = inputTitik(nVertex)
edges = ConnectEdge(vertices)

startVertex, targetVertex = inputStartTarget(vertices)

path = []
Path(edges, startVertex, targetVertex)

findShortestPath = findShortestPath(path)
print(findShortestPath)

for edge in findShortestPath:
    canvas.create_line(edge[0], edge[1], fill='red', width=3)
window.mainloop()