import csv
import collections
from numpy import array, double, size
edgeFile = 'edges.csv'
            
def ucs(start, end):
    # Begin your code (Part 3)
    """
    1.use dictionary with list to store adjacency list
    2.use ucs_path store each round of ucs search, visited store node which is visited
    3.use path to store node's predecessor
    4.In l35, if node not visited, store node into ucs_path for comparison
    5.In L41, if node != end, find min value of ucs_path, and set it as next predecessor
    6.if node's child is not visited, add node's child to ucs path, change the distance
    7.if node is end node, store final distance in dist, and continue
    8.remove visited node from ucs_path
    9.use a while looop to store shortest path
    """
    graph = collections.defaultdict(list)
    with open(edgeFile, 'r') as file:
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        for row in csvreader:
            graph[int(row[0])].append([int(row[1]), float(row[2])])

    dist = 0.0
    num_visited = 1
    ucs_path = []
    visited = []
    path = {}

    visited.append(start)

    for i in graph[start]:
        if i[0] not in visited:
            distance = i[1]
            node_num = i[0]
            ucs_path.append([distance, start, node_num])

    find = 0
    while find == 0 :
        node = min(ucs_path)
        if node[2] == end:
            path[node[2]] = node[1]
            visited.append(node[2])
            dist = node[0]
            find = 1
            continue

        if node[2] in visited:
            ucs_path.remove(node)
            continue

        elif node[2] in graph:
            visited.append(node[2])
            num_visited += 1
            path[node[2]] = node[1]
            for j in graph[node[2]]:
                if j[0] not in visited:
                    distance = j[1] + node[0]
                    node_num = j[0] 
                    ucs_path.append([distance, node[2], node_num])
        
        ucs_path.remove(node)

    shortest_path = []
    temp = end
    while temp != start:
        shortest_path.insert(1, temp)
        temp = path[temp]
    shortest_path.insert(1,start)

    return shortest_path, dist, num_visited

    #raise NotImplementedError("To be implemented")
    # End your code (Part 3)

if __name__ == '__main__':
    path, dist, num_visited = ucs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
