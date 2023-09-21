import sys

NO_PATH = sys.maxsize


def floyd_recursive_optimized(distance):
    num_nodes = len(distance)

    def recursive_floyd(start_node, end_node, intermediate):
        if intermediate == 0:
            return distance[start_node][end_node]

        without_intermediate = recursive_floyd(start_node, end_node, intermediate - 1)
        with_intermediate = (
                recursive_floyd(start_node, intermediate, intermediate - 1) +
                recursive_floyd(intermediate, end_node, intermediate - 1)
        )

        result = min(without_intermediate, with_intermediate)

        return result

    for intermediate in range(num_nodes):
        for start_node in range(num_nodes):
            for end_node in range(num_nodes):
                # Calculate the new distance
                new_distance = recursive_floyd(start_node, end_node, intermediate)
                # Update distances unconditionally
                distance[start_node][end_node] = new_distance

    return distance
