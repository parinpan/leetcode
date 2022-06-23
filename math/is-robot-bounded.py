# Leetcode: https://leetcode.com/problems/robot-bounded-in-circle/

def isRobotBounded(instructions):
    current_loc = [0, 0]
    current_facing = 'N'

    facing_map = {
        'L': {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'},
        'R': {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
    }

    axis_map = {
        'N': [0, 1],
        'E': [1, 1],
        'S': [0, -1],
        'W': [1, -1],
    }

    for command in instructions * 4:
        if command != 'G': 
            current_facing = facing_map[command][current_facing]
        else:
            axis, move = axis_map[current_facing]
            current_loc[axis] += move

    return current_loc == [0, 0]


if __name__ == '__main__':
    assert isRobotBounded("GGLLGG") == True
    assert isRobotBounded("GG") == False
    assert isRobotBounded("GL") == True
