def move_block(state, block, target):
    if state[block] == target:
        return state
    new_state = state.copy()
    new_state[block] = target
    return new_state

def is_goal_state(state, goal_state):
    return state == goal_state

def search(initial_state, goal_state):
    frontier = [initial_state]
    explored = set()

    while frontier:
        current_state = frontier.pop(0)
        explored.add(tuple(current_state.items()))

        if is_goal_state(current_state, goal_state):
            return True

        for block, on_block in current_state.items():
            if on_block != 'table':
                new_state = move_block(current_state, block, 'table')
                if new_state and tuple(new_state.items()) not in explored:
                    frontier.append(new_state)
                for other_block, other_on_block in current_state.items():
                    if other_on_block == 'table' and other_block != block:
                        new_state = move_block(current_state, block, other_block)
                        if new_state and tuple(new_state.items()) not in explored:
                            frontier.append(new_state)

    return False

# Example Usage
initial_state = {'A': 'B', 'B': 'C', 'C': 'table'}
goal_state = {'A': 'table', 'B': 'A', 'C': 'B'}

if search(initial_state, goal_state):
    print("Goal state reached!")
else:
    print("Goal state not reachable.")
