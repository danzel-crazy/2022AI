import csv
import collections
from numpy import array, double, size
edgeFile = 'edges.csv'
            
def dfs(start, end):
    
    # Begin your code (Part 1)
    """
    1. use the same adjacency list in bfs to store node
    2.l25 use line to implement stack, which pop means stack.pop() and append means stack.push()
    3.l31 store the top node in visited which means the node is already visited
    4.L35 iterate the node's children, if child equals to end point, give the state find 1
    5.l41 if children is not in visited list, add to stack, whilch implement dfs core
    6.L48~55 is usede to calculate distance and the path of dfs
    """
    num_visited = 0
    pre = {}
    graph = collections.defaultdict(list)
    with open(edgeFile, 'r') as file:
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        for row in csvreader:
            graph[int(row[0])].append([int(row[1]), float(row[2])])

    find = 0
    line = []
    line.append(start)
    visited_node = []
    visited_node.append(start)
    while ((len(line) != 0) & find != 1): 
        node = line.pop()
        visited_node.append(node)
        num_visited += 1
        # print(node)
        for i in graph[node]:
                if(i[0] == end) :   
                    pre[i[0]] = [node, i[1]]
                    find = 1 

                elif  i[0] not in visited_node:
                    pre[i[0]] = [node, i[1]]
                    line.append(i[0])
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
    path, dist, num_visited = dfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
