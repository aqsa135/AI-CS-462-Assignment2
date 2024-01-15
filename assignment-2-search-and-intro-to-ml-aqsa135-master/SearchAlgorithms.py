#Aqsa

from collections import deque

from MarsState import MarsState
from VacuumState import VacuumState
from RomaniaState import *
from HopperState import *
from HopperState import HopperState
import math


from queue import PriorityQueue


def breadth_first_search(startState, use_closed_list=True):
    search_queue = deque()
    closed_list = {}

    search_queue.append(startState)
    if use_closed_list:
        closed_list[startState] = True

    while len(search_queue) > 0:
        next_state = search_queue.popleft()
        if next_state.is_goal():
            print("Goal found")
            next_state.print_solution()
            print("Number of states generated:", len(closed_list))
            return
        else:
            successors = next_state.successors()
            if use_closed_list:
                successors = [item for item in successors if item not in closed_list]
                for s in successors:
                    closed_list[s] = True
            search_queue.extend(successors)


def depth_first_search(startState, use_closed_list=True, limit=20):
    search_stack = deque()
    closed_list = {}

    search_stack.append(startState)
    if use_closed_list:
        closed_list[startState] = True

    while len(search_stack) > 0:
        next_state = search_stack.pop()
        if next_state.is_goal():
            print("Goal found")
            next_state.print_solution()
            print("Number of states generated:", len(closed_list))
            return True
        elif next_state.cost < limit:
            successors = next_state.successors()
            if use_closed_list:
                successors = [item for item in successors if item not in closed_list]
                for s in successors:
                    closed_list[s] = True
            search_stack.extend(successors)
    return False


def iterative_deepening_search(startState):
    limit = 1
    while True:
        print(f"Trying with limit: {limit}")
        if depth_first_search(startState, limit=limit):
            break
        limit += 1


def a_star(startState, heuristic_fn, use_closed_list=True):
    search_queue = PriorityQueue()
    closed_list = {}
    search_queue.put((0 + heuristic_fn(startState), startState))

    while not search_queue.empty():
        cost, current_state = search_queue.get()
        if current_state.is_goal():
            print("Goal found")
            current_state.print_solution()
            print("Number of states generated:", len(closed_list))
            return

        if current_state not in closed_list or cost < closed_list[current_state]:
            closed_list[current_state] = cost
            for successor in current_state.successors():
                if successor not in closed_list:
                    f_cost = successor.cost + heuristic_fn(successor)
                    search_queue.put((f_cost, successor))



## simulate uniform cost
def h1(s) :
    return 0

## implement this for the Mars rover.
# def SLD(s1, s2):
#     coords1 = tuple(map(int, s1.location.split(',')))
#     coords2 = tuple(map(int, s2.location.split(',')))
#     return math.sqrt((coords1[0] - coords2[0]) ** 2 + (coords1[1] - coords2[1]) ** 2)

def SLD(s1, s2):
    x1, y1 = map(int, s1.location.split(','))
    x2, y2 = map(int, s2.location.split(','))
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

## SLD to Bucharest
def RomaniaSLD(s) :
    slds = {'Arad':366, 'Bucharest':0,'Craiova':166,'Dobreta':242,
    'Eforie':161, 'Fagaras':176, 'Giurgiu':77, 'Hirsova':151,
    'Iasi':226, 'Lugoj':244, 'Mehadia':241, 'Neamt':234, 'Oradea':380,
    'Pitesti':100, 'Rimnicu Vilcea':193, 'Sibiu':253, 'Timisoara':329,
    'Urziceni':80, 'Vaslui':199, 'Zerind':374}
    return slds[s.location]



if __name__ == "__main__" :
    #start = VacuumState('left',False,False)
    # g = make_romania_graph()
    # start = RomaniaState('Arad',g)
    # start = HopperState(0,0,0)
    # breadth_first_search(start, True)
    # depth_first_search(start, True)
    # a_star(start, h1, True)
    start = HopperState(0, 0, 0)

    print("Running BFS:")
    breadth_first_search(start, True)

    print("\nRunning DFS:")
    depth_first_search(start, use_closed_list=True, limit=20)

    print("\nRunning DLS with limit 10:")
    depth_first_search(start, use_closed_list=True, limit=10)

    print("\nRunning Iterative Deepening Search:")
    iterative_deepening_search(start)
    # mars_state = MarsState()
    # mars_state.read_mars_graph("MarsMap")
    #
    # print("Running A* Search:")
    # # Run A* Search on the MarsMap
    # a_star(mars_state, SLD, True)
    #
    # print("\nRunning Uniform Cost Search:")
    # # Run Uniform Cost Search (i.e., A* with h1 as heuristic) on the MarsMap
    # a_star(mars_state, h1, True)
    # marsGraph = MarsState()
    # marsGraph.read_mars_graph("MarsMap")
    #
    # # Assuming the start location is '2,1' for example
    # start = MarsState(location='2,1', mars_graph=marsGraph.mars_graph)
    # goal = MarsState(location='1,1', mars_graph=marsGraph.mars_graph)
    #
    # a_star(start, lambda state: SLD(state, goal), True)
    marsGraph = MarsState()
    marsGraph.read_mars_graph("MarsMap")

    start = MarsState(location='2,1', mars_graph=marsGraph.mars_graph)
    goal = MarsState(location='1,1', mars_graph=marsGraph.mars_graph)

    print("Running A* Search:")
    a_star(start, lambda state: SLD(state, goal), True)

    print("\nRunning Uniform Cost Search:")
    a_star(start, h1, True)


