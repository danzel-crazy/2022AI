import csv
import queue 
import collections
from numpy import array, double
edgeFile = 'edges.csv'
            
def bfs(start, end):
    
    # Begin your code (Part 1)
    """
    1.use csv.reader to read .csv
    2.use graph to construct an adjacency list
    3.use queue to implement bfs, visited_node to store visited node
    4.queue.get obtain the top element in queue
    5.if node == end, break
    6.use pre to store each node's parent
    7.store bfs in list of path and compute distance
    """
    num_visited = 0
    pre = {}
    q = queue.Queue()
    graph = collections.defaultdict(list)
    with open(edgeFile, 'r') as file:
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        for row in csvreader:
            graph[int(row[0])].append([int(row[1]), float(row[2])])
        
        # print(graph[26059311])

    find = 0
    q.put(start)
    visited_node = []
    visited_node.append(start)
    while ((q.empty() == 0) & find != 1): 
        node = q.get()
        # print(node)

        for i in graph[node]:
            if find == 0:
                if(i[0] == end):
                    pre[i[0]] = [node, 0]
                    # with q.mutex:
                    #     q.queue.clear()
                    find = 1   

                if i[0] not in visited_node:
                    num_visited += 1
                    visited_node.append(i[0])
                    pre[i[0]] = [node, i[1]]
                    q.put(i[0])

    # for i in pre :
    #     print(pre[i])

    distance = 0.0
    temp = end
    path = []
    while(temp != start) : 
        path.insert(1, temp)
        distance += pre[temp][1]
        temp = pre[temp][0]
    path.insert(1,start)
    
    # print(len(path))
    # print(distance)
    # print(num_visited)
    
    return path, distance, num_visited
    
    
    # raise NotImplementedError("To be implemented")
    
    # End your code (Part 1)
if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
