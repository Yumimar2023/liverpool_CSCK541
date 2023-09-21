import unittest
import sys
from floyds_recursive import floyd_recursive_optimized

NO_PATH = sys.maxsize


# Define test cases for different scenarios
class TestFloydRecursive(unittest.TestCase):
    def test_shortest_paths(self):
        # Test case with a regular graph
        graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        result = floyd_recursive_optimized(graph)
        expected = [
            [0, 7, 12, 8],
            [sys.maxsize, 0, 5, 7],
            [sys.maxsize, sys.maxsize, 0, 2],
            [sys.maxsize, sys.maxsize, sys.maxsize, 0]
        ]
        self.assertEqual(result, expected)

    def test_single_vertex(self):
        # Test case with a single vertex graph
        single_vertex_graph = [[0]]
        result = floyd_recursive_optimized(single_vertex_graph)
        expected = [[0]]
        self.assertEqual(result, expected)

    def test_negative_weights(self):
        # Test case with a square graph containing negative weights
        graph = [
            [0, -1, 1],
            [sys.maxsize, 0, sys.maxsize],
            [sys.maxsize, 2, 0]
        ]
        result = floyd_recursive_optimized(graph)
        expected = [
            [0, -1, 1],
            [sys.maxsize, 0, sys.maxsize],
            [sys.maxsize, 2, 0]
        ]
        self.assertEqual(result, expected)


    def test_graph_with_duplicate_paths(self):
        # Test case with a graph containing duplicate paths
        graph = [
            [0, 1, 1],
            [NO_PATH, 0, NO_PATH],
            [NO_PATH, 1, 0]
        ]
        result = floyd_recursive_optimized(graph)
        expected = [
            [0, 1, 1],
            [NO_PATH, 0, NO_PATH],
            [NO_PATH, 1, 0]
        ]
        self.assertEqual(result, expected)

    def test_graph_with_disconnected_components(self):
        # Test case with disconnected components in the graph
        graph = [
            [0, 1, NO_PATH, NO_PATH],
            [1, 0, NO_PATH, NO_PATH],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, 1, 0]
        ]
        result = floyd_recursive_optimized(graph)
        expected = [
            [0, 1, NO_PATH, NO_PATH],
            [1, 0, NO_PATH, NO_PATH],
            [NO_PATH, NO_PATH, 0, 1],
            [NO_PATH, NO_PATH, 1, 0]
        ]
        self.assertEqual(result, expected)

    def test_graph_with_negative_cycle(self):
        # Test case with a graph containing a negative cycle
        graph = [
            [0, -1, 1],
            [1, 0, 1],
            [-1, -1, 0]
        ]
        result = floyd_recursive_optimized(graph)

        # Check if there is any negative value in the resulting matrix
        has_negative_cycle = any(any(distance < 0 for distance in row) for row in result)

        self.assertTrue(has_negative_cycle, "Negative Cycle Detected")

if __name__ == '__main__':
    unittest.main()
