heuristicFile = 'heuristic.csv'
import csv
import collections
from numpy import array, double, size
edgeFile = 'edges.csv'
            
def astar(start, end):
    # Begin your code (Part 3)
    """
    1.use graph to store adjacency list and use h to store heuristic value for each node
    2.create open and close list to store node for astar search, first push start to opened
    3.use g{} ot store the distance for astar search, if node's distance < g[n] + g[i], refresh distance
    4.In while loop, find the small n with g[n]
    5.if n == end, store dist = g[n]
    6.In L53, if node is not in open or close, add node to open and store g[n] base on previous node
    7.if node is in opened, store it in to path with its predecesspr
    8.if node in closed and distance need to refresh, put it back to open to revaluate
    9.push n to closed and remove from open
    10.use while loop to store astar path
    """
    graph = collections.defaultdict(list)
    
    with open(edgeFile, 'r') as file:
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        for row in csvreader:
            graph[int(row[0])].append([int(row[1]), float(row[2])])
            
    h = {}
    with open(heuristicFile, 'r') as file:
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        for row in csvreader:
            h[int(row[0])] = float(row[3])
    
    num_visited = 0
    opened = set([start]) 
    closed = set()

    g = {} 
    g[start] = 0

    path = {}
    
    while len(opened) > 0:
        n = None
        for v in opened:
            if n == None or g[n] + h[n] > g[v] + h[v]:
                n = v
        if n == end:
            dist = g[n]
            break;
        for i in graph[n]:
            if i[0] not in opened and i[0] not in closed:
                num_visited += 1
                opened.add(i[0])
                path[i[0]] = n
                g[i[0]] = g[n] + i[1]
            
            else:
                if g[i[0]] > g[n] + i[1]:
                    g[i[0]] = g[n] + i[1]
                    path[i[0]] = n

                    if i[0] in closed:
                        closed.remove(i[0])
                        opened.add(i[0])
        
        opened.remove(n)
        closed.add(n)
        
    
    temp = end
    shortest_path = []
    while temp != start:
        temp = path[temp]
        shortest_path.insert(1, temp)
    shortest_path.insert(1,start)

    return shortest_path, dist, num_visited      
    #raise NotImplementedError("To be implemented")
    # End your code (Part 4)


if __name__ == '__main__':
    path, dist, num_visited = astar(1718165260, 8513026827)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
