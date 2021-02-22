from collections import deque


# Information *****************************************************


class PuzzleState:
    def __init__(self, state, parent, move, depth, cost, key):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        if self.state:
            self.map = ''.join(str(e) for e in self.state)

    def __eq__(self, other):
        return self.map == other.map

    def __lt__(self, other):
        return self.map < other.map

    def __str__(self):
        return str(self.map)


# Global variables***********************************************


GoalState = [0, 1, 2, 3, 4, 5, 6, 7, 8]
GoalNode = None  # at finding solution
NodesExpanded = 0  # total nodes visited
MaxSearchDeep = 0  # max deep
MaxFrontier = 0  # max frontier


# BFS**************************************************************
def bfs(start_state):
    global MaxFrontier, GoalNode, MaxSearchDeep

    board_visited = set()
    queue = deque([PuzzleState(start_state, None, None, 0, 0, 0)])

    while queue:
        node = queue.popleft()
        board_visited.add(node.map)
        if node.state == GoalState:
            GoalNode = node
            return queue
        possible_paths = sub_nodes(node)
        for path in possible_paths:
            if path.map not in board_visited:
                queue.append(path)
                board_visited.add(path.map)
                if path.depth > MaxSearchDeep:
                    MaxSearchDeep = MaxSearchDeep + 1
        if len(queue) > MaxFrontier:
            queue_size = len(queue)
            MaxFrontier = queue_size


# Obtain Sub Nodes********************************************************
def sub_nodes(node):
    global NodesExpanded
    NodesExpanded = NodesExpanded + 1

    next_paths = []
    next_paths.append(PuzzleState(move(node.state, 1), node, 1, node.depth + 1, node.cost + 1, 0))
    next_paths.append(PuzzleState(move(node.state, 2), node, 2, node.depth + 1, node.cost + 1, 0))
    next_paths.append(PuzzleState(move(node.state, 3), node, 3, node.depth + 1, node.cost + 1, 0))
    next_paths.append(PuzzleState(move(node.state, 4), node, 4, node.depth + 1, node.cost + 1, 0))
    nodes = []
    for proc_paths in next_paths:
        if proc_paths.state is not None:
            nodes.append(proc_paths)
    return nodes


# Next step**************************************************************
def move(state, direction):
    # generate a copy
    new_state = state[:]

    # obtain poss of 0
    index = new_state.index(0)

    if index == 0:
        if direction == 1:
            return None
        if direction == 2:
            temp = new_state[0]
            new_state[0] = new_state[3]
            new_state[3] = temp
        if direction == 3:
            return None
        if direction == 4:
            temp = new_state[0]
            new_state[0] = new_state[1]
            new_state[1] = temp
        return new_state
    if index == 1:
        if direction == 1:
            return None
        if direction == 2:
            temp = new_state[1]
            new_state[1] = new_state[4]
            new_state[4] = temp
        if direction == 3:
            temp = new_state[1]
            new_state[1] = new_state[0]
            new_state[0] = temp
        if direction == 4:
            temp = new_state[1]
            new_state[1] = new_state[2]
            new_state[2] = temp
        return new_state
    if index == 2:
        if direction == 1:
            return None
        if direction == 2:
            temp = new_state[2]
            new_state[2] = new_state[5]
            new_state[5] = temp
        if direction == 3:
            temp = new_state[2]
            new_state[2] = new_state[1]
            new_state[1] = temp
        if direction == 4:
            return None
        return new_state
    if index == 3:
        if direction == 1:
            temp = new_state[3]
            new_state[3] = new_state[0]
            new_state[0] = temp
        if direction == 2:
            temp = new_state[3]
            new_state[3] = new_state[6]
            new_state[6] = temp
        if direction == 3:
            return None
        if direction == 4:
            temp = new_state[3]
            new_state[3] = new_state[4]
            new_state[4] = temp
        return new_state
    if index == 4:
        if direction == 1:
            temp = new_state[4]
            new_state[4] = new_state[1]
            new_state[1] = temp
        if direction == 2:
            temp = new_state[4]
            new_state[4] = new_state[7]
            new_state[7] = temp
        if direction == 3:
            temp = new_state[4]
            new_state[4] = new_state[3]
            new_state[3] = temp
        if direction == 4:
            temp = new_state[4]
            new_state[4] = new_state[5]
            new_state[5] = temp
        return new_state
    if index == 5:
        if direction == 1:
            temp = new_state[5]
            new_state[5] = new_state[2]
            new_state[2] = temp
        if direction == 2:
            temp = new_state[5]
            new_state[5] = new_state[8]
            new_state[8] = temp
        if direction == 3:
            temp = new_state[5]
            new_state[5] = new_state[4]
            new_state[4] = temp
        if direction == 4:
            return None
        return new_state
    if index == 6:
        if direction == 1:
            temp = new_state[6]
            new_state[6] = new_state[3]
            new_state[3] = temp
        if direction == 2:
            return None
        if direction == 3:
            return None
        if direction == 4:
            temp = new_state[6]
            new_state[6] = new_state[7]
            new_state[7] = temp
        return new_state
    if index == 7:
        if direction == 1:
            temp = new_state[7]
            new_state[7] = new_state[4]
            new_state[4] = temp
        if direction == 2:
            return None
        if direction == 3:
            temp = new_state[7]
            new_state[7] = new_state[6]
            new_state[6] = temp
        if direction == 4:
            temp = new_state[7]
            new_state[7] = new_state[8]
            new_state[8] = temp
        return new_state
    if index == 8:
        if direction == 1:
            temp = new_state[8]
            new_state[8] = new_state[5]
            new_state[5] = temp
        if direction == 2:
            return None
        if direction == 3:
            temp = new_state[8]
            new_state[8] = new_state[7]
            new_state[7] = temp
        if direction == 4:
            return None
        return new_state


def get_solution(puzzle_board):
    global GoalNode
    initial_state = puzzle_board
    solution = []

    # Start operation

    bfs(initial_state)

    # Save total path result
    deep = GoalNode.depth
    moves = []
    while initial_state != GoalNode.state:
        if GoalNode.move == 1:
            path = 'Up'
        if GoalNode.move == 2:
            path = 'Down'
        if GoalNode.move == 3:
            path = 'Left'
        if GoalNode.move == 4:
            path = 'Right'
        moves.insert(0, path)
        GoalNode = GoalNode.parent

        # get results
        path = moves
        cost = len(moves)
        nodes_expanded = str(NodesExpanded)
        search_depth = str(deep)

    solution.append({
        "path": path,
        "cost": cost,
        "nodes_expanded": nodes_expanded,
        "search_depth": search_depth
    })

    return solution
