from State import State

class VacuumState(State) :
    def __init__(self, location='left', leftClean=True, rightClean=True,
                 prev_state=None, prev_action=None):
        self.location = location
        self.leftClean = leftClean
        self.rightClean=rightClean
        self.prev_state = prev_state
        self.prev_action = prev_action
        if prev_state :
            self.cost = prev_state.cost + 1
        else :
            self.cost = 0

    def __eq__(self,other):
        return self.location == other.location and self.leftClean == other.leftClean and self.rightClean == other.rightClean

    def __hash__(self):
        return hash(self.__repr__())

    def __repr__(self):
        return "(%s %s %s)" % (self.location, self.leftClean, self.rightClean)

    def is_goal(self):
        return self.leftClean and self.rightClean

    ## print in reverse
    def print_solution(self):
        ptr = self
        print(ptr)
        while ptr :
            print(ptr.prev_action)
            print(ptr.prev_state)
            ptr = ptr.prev_state

    ## we can take three actions: move left, move right, suck up the dirt.
    ## in some cases, an action will have no effect. In that case, we will ignore it.

    def successors(self):
        succ_list = []
        if self.location == 'left':
            succ_list.append(VacuumState('right', self.leftClean, self.rightClean, self, 'move_right'))
        else :
            succ_list.append(VacuumState('left', self.leftClean, self.rightClean, self, 'move_left'))
        if self.location == 'left' and self.leftClean == False :
            succ_list.append(VacuumState(self.location, True, self.rightClean, self, 'suck'))
        if self.location == 'right' and self.rightClean == False:
            succ_list.append(VacuumState(self.location, self.leftClean, True, self, 'suck'))
        return succ_list