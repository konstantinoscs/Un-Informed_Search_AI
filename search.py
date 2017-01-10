# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]

# NOTE TO INSTRUCTORS: I will try to generalize my search algorithm so each implementation
# differs only slightly

def depthFirstSearch(problem):

    solution = []
    revsol = util.Stack()  # reverse solution
    fringe = util.Stack()
    closed = set()
    find = {}  # dict of {node:(parent, action, cost)} items

    """Search the deepest nodes in the search tree first."""

    start_state = problem.getStartState()
    state = start_state
    if problem.isGoalState(state):
        return solution

    if state not in closed:
        closed.add(state)
        successors = [i + (state,) for i in problem.getSuccessors(state)]
        print successors
        for i in successors:
            if i[0] not in closed:
                fringe.push(i)

    if fringe.isEmpty():
        return None

    while not fringe.isEmpty():
        node = fringe.pop()
        state = node[0]

        if problem.isGoalState(state):
            find[state] = (node[3], node[1], node[2])  # found solution but not updated the dict
            break

        if state not in closed:
            closed.add(state)
            find[state] = (node[3], node[1], node[2])
            successors = [i + (state,) for i in problem.getSuccessors(state)]
            for i in successors:
                if i[0] not in closed:
                    fringe.push(i)

    if problem.isGoalState(state):
        dnode = find[state]  # dict node
        prev = dnode[0]
        action = dnode[1]
        revsol.push(action)

        while prev != start_state:
            dnode = find[prev]
            prev = dnode[0]
            action = dnode[1]
            revsol.push(action)

        while not revsol.isEmpty():
            solution.append(revsol.pop())

        return solution

        # dnode[2] useless for dfs/bfs
    else:
        return None


def breadthFirstSearch(problem):
    solution = []
    revsol = util.Stack()  # reverse solution
    fringe = util.Queue()
    closed = set()
    find = {}  # dict of {node:(parent, action, cost)} items
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    start_state = problem.getStartState()
    state = start_state
    if problem.isGoalState(state):
        return solution

    if state not in closed:
        closed.add(state)
        successors = [i + (state,) for i in problem.getSuccessors(state)]
        for i in successors:
            if i[0] not in closed:
                fringe.push(i)

    if fringe.isEmpty():
        return None

    while not fringe.isEmpty():
        node = fringe.pop()
        state = node[0]

        if problem.isGoalState(state):
            find[state] = (node[3], node[1], node[2])  # found solution but not updated the dict
            break

        if state not in closed:
            closed.add(state)
            find[state] = (node[3], node[1], node[2])
            successors = [i + (state,) for i in problem.getSuccessors(state)]
            for i in successors:
                if i[0] not in closed:
                    fringe.push(i)

    if problem.isGoalState(state):
        dnode = find[state]  # dict node
        prev = dnode[0]
        action = dnode[1]
        revsol.push(action)

        while prev != start_state:
            dnode = find[prev]
            prev = dnode[0]
            action = dnode[1]
            revsol.push(action)

        while not revsol.isEmpty():
            solution.append(revsol.pop())

        return solution

        # dnode[2] useless for dfs/bfs
    else:
        return None

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    solution = []
    revsol = util.Stack()  # reverse solution
    fringe = util.PriorityQueue()
    closed = set()
    find = {}  # dict of {node:(parent, action, cost)} items

    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    state = start_state
    if problem.isGoalState(state):
        return solution

    if state not in closed:
        closed.add(state)
        successors = [i + (state,) for i in problem.getSuccessors(state)]
        for i in successors:
            if i[0] not in closed:
                fringe.update(i, i[2])

    if fringe.isEmpty():
            return None

    while not fringe.isEmpty():
        node = fringe.pop()
        state = node[0]

        if problem.isGoalState(state):
            find[state] = (node[3], node[1], node[2])  # found solution but not updated the dict
            break

        if state not in closed:
            closed.add(state)
            find[state] = (node[3], node[1], node[2])
            successors = [i + (state,) for i in problem.getSuccessors(state)]
            for i in successors:
                if i[0] not in closed:
                    tot_cost = i[2] + find[state][2]
                    i = list(i)
                    i[2] = tot_cost
                    i = tuple(i)
                    fringe.update(i, tot_cost)

    if problem.isGoalState(state):
        dnode = find[state]  # dict node
        prev = dnode[0]
        action = dnode[1]
        revsol.push(action)

        while prev != start_state:
            dnode = find[prev]
            prev = dnode[0]
            action = dnode[1]
            revsol.push(action)

        while not revsol.isEmpty():
             solution.append(revsol.pop())

        return solution
    else:
        return None

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    solution = []
    revsol = util.Stack()  # reverse solution
    fringe = util.PriorityQueue()
    closed = set()
    find = {}  # dict of {node:(parent, action, cost)} items

    "*** YOUR CODE HERE ***"
    start_state = problem.getStartState()
    state = start_state
    if problem.isGoalState(state):
        return solution

    if state not in closed:
        closed.add(state)
        successors = [i + (state,) for i in problem.getSuccessors(state)] # (state, action, cost, parent)
        for i in successors:
            if i[0] not in closed:
                tot_cost = i[2] + heuristic(i[0], problem)  # difference from ucs, add the heuristic
                fringe.update(i, tot_cost)

    if fringe.isEmpty():
            return None

    while not fringe.isEmpty():
        node = fringe.pop()
        state = node[0]

        if problem.isGoalState(state):
            find[state] = (node[3], node[1], node[2])  # found solution but not updated the dict
            break

        if state not in closed:
            closed.add(state)
            find[state] = (node[3], node[1], node[2])
            successors = [i + (state,) for i in problem.getSuccessors(state)]
            for i in successors:
                if i[0] not in closed:
                    tot_cost = i[2] + find[state][2]
                    i = list(i)
                    i[2] = tot_cost
                    i = tuple(i)
                    tot_cost += heuristic(i[0], problem)  # difference from ucs, add the heuristic to cost
                    fringe.update(i, tot_cost)

    if problem.isGoalState(state):
        dnode = find[state]  # dict node
        prev = dnode[0]
        action = dnode[1]
        revsol.push(action)

        while prev != start_state:
            dnode = find[prev]
            prev = dnode[0]
            action = dnode[1]
            revsol.push(action)

        while not revsol.isEmpty():
             solution.append(revsol.pop())

        return solution
    else:
        return None


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
