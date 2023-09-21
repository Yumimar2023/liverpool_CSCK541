import sys
import time
from floyds_recursive import floyd_recursive_optimized
from floyds_imperative import floyd

# Set a higher recursion limit (adjust as needed)
sys.setrecursionlimit(10 ** 3)


# This function will run the code and record the time
def compare_performance():
    # Helper script
    NO_PATH = sys.maxsize
    graph = [
        [0, 7, NO_PATH, 8],
        [NO_PATH, 0, 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
    ]

    record_time = time.time()
    for _ in range(2 ** 12):
        floyd_recursive_optimized([row[:] for row in graph])
    elapsed_time_recursive = time.time() - record_time

    record_time = time.time()
    for _ in range(2 ** 12):
        floyd([row[:] for row in graph])
    elapsed_time_imperative = time.time() - record_time

    return elapsed_time_recursive, elapsed_time_imperative


if __name__ == '__main__':
    elapsed_recursive, elapsed_imperative = compare_performance()
    print('Recursive: {}s'.format(round(elapsed_recursive, 2)))
    print('Imperative: {}s'.format(round(elapsed_imperative, 2)))
