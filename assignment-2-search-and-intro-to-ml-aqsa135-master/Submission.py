
from HopperState import HopperState, hopper1max, hopper2max, hopper3max
import sklearn_intro
from MarsState import MarsState
from SearchAlgorithms import breadth_first_search, depth_first_search, iterative_deepening_search


def main():
    print("Testing HopperState Class...")

    # Creating an instance of HopperState
    h = HopperState(hopper1max, hopper2max, hopper3max)
    print("Initial HopperState:", h)

    # Testing successors method
    print("\nGenerating Successors...")
    successors = h.successors()
    for succ in successors:
        print("Action:", succ.prev_action, "| Resulting State:", succ)

    # # Testing goal state check
    # goal_state = HopperState(4, 4, 0)
    # print("\nIs goal state?", goal_state.is_goal())

    # Testing equality and hash functions
    h1 = HopperState(8, 5, 3)
    h2 = HopperState(8, 5, 3)
    print("\nTesting Equality and Hash:")
    print("h1 == h2?", h1 == h2)
    print("hash(h1) == hash(h2)?", hash(h1) == hash(h2))

    print(sklearn_intro)

    # Create an instance of MarsState and call its read_mars_graph method
    mars_state = MarsState()
    mars_state.read_mars_graph("MarsMap")

    # Print the graph attribute of the MarsState object
    print(mars_state.mars_graph.g)

    # BFS,DFS,DLS, IDS
    start = HopperState(0, 0, 0)

    print("Running BFS:")
    breadth_first_search(start, True)

    print("\nRunning DFS:")
    depth_first_search(start, use_closed_list=True, limit=20)

    print("\nRunning DLS with limit 10:")
    depth_first_search(start, use_closed_list=True, limit=10)

    print("\nRunning Iterative Deepening Search:")
    iterative_deepening_search(start)


if __name__ == '__main__':
    main()