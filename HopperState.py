
from State import State

hopper1max = 8
hopper2max = 5
hopper3max = 3

class HopperState(State) :
    counter = 0

    def __init__(self, h1=0,h2=0,h3=0, prev_state=None, prev_action=None):
        State.__init__(self)
        HopperState.counter=HopperState.counter + 1
        self.hopper1 = h1
        self.hopper2 = h2
        self.hopper3 = h3
        self.prev_state = prev_state
        self.prev_action = prev_action
        if prev_state :
            self.cost = prev_state.cost + 1
        else :
            self.cost = 0

## you do this.
    def __eq__(self, other):
        return isinstance(other,
                          HopperState) and self.hopper1 == other.hopper1 and self.hopper2 == other.hopper2 and self.hopper3 == other.hopper3

## you do this
    def __lt__(self, other):

        return self.cost < other.cost


## you do this
    def __hash__(self):
        return hash((self.hopper1, self.hopper2, self.hopper3))

    def __repr__(self):
        return "(hopper1 %i hopper2 %i hopper3 %i)" % \
               (self.hopper1, self.hopper2, self.hopper3)

    def is_goal(self):
        return self.hopper1 == 4 and \
               self.hopper2 == 0 and\
               self.hopper3 == 0

    def print_solution(self):
        ptr = self
        print(ptr)
        while ptr :
            print(ptr.prev_action)
            print(ptr.prev_state)
            ptr = ptr.prev_state
        print("Number of states: %i" % HopperState.counter)

    def successors(self):
        successors = []

        hoppers = [(self.hopper1, hopper1max), (self.hopper2, hopper2max), (self.hopper3, hopper3max)]

        for i, (current, max_value) in enumerate(hoppers):
            if current < max_value:
                new_hoppers = hoppers.copy()
                new_hoppers[i] = (max_value, max_value)  # Fix here: Change to new_hoppers[i] = (max_value, max_value)
                successors.append(HopperState(*[h[0] for h in new_hoppers], self, f"Fill Hopper {i + 1}"))

            if current > 0:
                new_hoppers = hoppers.copy()
                new_hoppers[i] = (0, max_value)
                successors.append(HopperState(*[h[0] for h in new_hoppers], self, f"Dump Hopper {i + 1}"))

        for i, (current, _) in enumerate(hoppers):
            for j, (target, target_max) in enumerate(hoppers):
                if i != j and current > 0 and target < target_max:
                    amount = min(current, target_max - target)
                    new_hoppers = hoppers.copy()
                    new_hoppers[i] = (current - amount, hoppers[i][1])
                    new_hoppers[j] = (target + amount, hoppers[j][1])
                    successors.append(HopperState(*[h[0] for h in new_hoppers], self, f"Pour from {i + 1} to {j + 1}"))

        return successors


if __name__ == '__main__' :
    h1 = HopperState(8,5,3)
    h2 = HopperState(8,5,3)
    if (h1 == h2) :
        print("it works!")


