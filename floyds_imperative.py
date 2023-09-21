import sys
import itertools

"""The following is a distance matrix. Each list is the distance between that node and the rest of the nodes. 
For example graph[0] is the distance between node 0 and nodes 0,1,2 and 3. 
Unsurprisingly the distance between Node 0 and Node 0 is 0, whereas between Node 0 and Node 1 is 7. 
NO_PATH indicates that there is no direct path."""

NO_PATH = sys.maxsize
graph = [[0, 7, NO_PATH, 8], [NO_PATH, 0, 5, NO_PATH], [NO_PATH, NO_PATH, 0, 2], [NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])


def floyd(distance):
    """A simple implementation of Floyd's algorithm"""
    for intermediate, start_node, end_node in itertools.product(range(MAX_LENGTH), range(MAX_LENGTH),
                                                                range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] + distance[intermediate][end_node])
        # Any value that have sys.maxsize has no path
        print(distance)
    # floyd(graph) # Removed this line, as it's causing errors in performance testing


result = floyd(graph)