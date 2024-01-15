from Graph import Graph, Edge
from State import State


class RomaniaState(State) :
    def __init__(self, location="", romania_graph=None,
                 prev_state=None, cost=0):
        self.location = location
        self.romania_graph = romania_graph
        self.prev_state = prev_state
        self.cost=cost

    def __eq__(self,other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def is_goal(self):
        return self.location == 'Bucharest'

    ## print in reverse
    def print_solution(self):
        ptr = self
        print(ptr)
        while ptr :
            print(ptr.prev_state)
            ptr = ptr.prev_state

    def successors(self):
        edges = self.romania_graph.get_edges(self.location)
        return [RomaniaState(edge.dest, self.romania_graph, self,
                             self.cost+edge.val)
                for edge in edges]



def make_romania_graph() :
    cities = ['Arad', 'Bucharest', 'Craiova', 'Dobreta', 'Eforie',
              'Fagaras', 'Giorgiu', 'Hirsova', 'Iasi', 'Lugoj',
              'Mehadia', 'Neamt', 'Oradea', 'Pitesti',
              'Rimnicu Vilcea', 'Sibiu', 'Timisoara', 'Urziceni',
              'Vaslui', 'Zerind']


    edges = [('Arad','Zerind',75),('Arad','Sibiu', 140), ('Arad','Timisoara',118),
            ('Bucharest','Urziceni',85), ('Bucharest','Pitesti',101), ('Bucharest','Pitesti',101),('Bucharest','Giorgiu',90, 'Bucharest','Fagaras',211),
            ('Craiova','Dobreta', 120), ('Craiova','Rimnicu Vilcea',146), ('Craiova','Pitesti',138),
            ('Dobreta','Mehadia',75),
            ('Eforie','Hirsova',86),
            ('Fagaras','Sibiu',99),
            ('Hirsova', 'Urziceni',98),
            ('Iasi','Vaslui', 92), ('Iasi','Neamt', 87),
            ('Lugoj','Timisoara',111), ('Lugoj','Mehadia',70),
            ('Oradea','Zerind',71), ('Oradea', 'Sibiu', 151),

             ('Rimnicu Vilcea','Sibiu',80),('Rimnicu Vilcea','Pitesti',97),
            ('Urziceni', 'Vaslui',142)]

    g = Graph()
    for c in cities :
        g.add_node(c)

    for edge in edges :
        g.add_edge(Edge(edge[0],edge[1], edge[2]))
        g.add_edge(Edge(edge[1], edge[0],edge[2]))
    return g