class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action


def is_goal(node):
    return node.state == (0, 0, 'dreapta')


def actions(node):
    m, c, b = node.state
    actions = []
    if b == 'stânga':
        if m > 0:
            actions.append((-1, 0, 'dreapta'))
        if m > 1:
            actions.append((-2, 0, 'dreapta'))
        if m > 0 and c > 0:
            actions.append((-1, -1, 'dreapta'))
        if c > 0:
            actions.append((0, -1, 'dreapta'))
        if c > 1:
            actions.append((0, -2, 'dreapta'))
    else:
        if m < 3:
            actions.append((1, 0, 'stânga'))
        if m < 2:
            actions.append((2, 0, 'stânga'))
        if m < 3 and c < 3:
            actions.append((1, 1, 'stânga'))
        if c < 3:
            actions.append((0, 1, 'stânga'))
        if c < 2:
            actions.append((0, 2, 'stânga'))
    return actions


def result(node, action):
    m, c, b = node.state
    m2, c2, b2 = action
    return (m+m2, c+c2, b2)


def dfs():
    initial_state = (3, 5, 'stânga')
    initial_node = Node(initial_state)
    frontier = [initial_node]
    explored = set()
    while frontier:
        node = frontier.pop()
        if node.state in explored:
            continue
        explored.add(node.state)
        if is_goal(node):
            return node
        for action in actions(node):
            child = Node(result(node, action), node, action)
            frontier.append(child)
    return None


node = dfs()
if node is None:
    print("Nu există soluție.")
else:
    path = []
    while node.parent is not None:
        path.append(node.action)
        node = node.parent
    path.reverse()
    print("Soluție:", path)