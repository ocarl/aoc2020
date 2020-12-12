test_data = """F10
N3
F7
R90
F11"""


def turn(r_or_l, init_pos):
    if r_or_l == 'R':
        rotaion_matrix = [[0, 1], [-1, 0]]
    elif r_or_l == 'L':
        rotaion_matrix = [[0, -1], [1, 0]]
    x = init_pos[0]*rotaion_matrix[0][0] + init_pos[1]*rotaion_matrix[0][1]
    y = init_pos[0]*rotaion_matrix[1][0] + init_pos[1]*rotaion_matrix[1][1]
    return x, y


def solve(data):
    head_map = {
        'E': (1, 0),
        'N': (0, 1),
        'W': (-1, 0),
        'S': (0, -1),
    }
    waypoint_pos_x = 10
    waypoint_pos_y = 1
    ship_pos_x = 0
    ship_pos_y = 0
    for line in data.split('\n'):
        if 'F' in line:
            delta_x = int(line[1:])*waypoint_pos_x
            delta_y = int(line[1:])*waypoint_pos_y
            ship_pos_x += delta_x
            ship_pos_y += delta_y
        elif 'R' in line or 'L' in line:
            for _ in range(int(line[1:])//90):
                waypoint_pos_x, waypoint_pos_y = turn(line[0], (waypoint_pos_x, waypoint_pos_y))
        elif line[0] in ['N', 'E', 'S', 'W']:
            delta_x = int(line[1:]) * head_map[line[0]][0]
            delta_y = int(line[1:]) * head_map[line[0]][1]
            waypoint_pos_x += delta_x
            waypoint_pos_y += delta_y
    return abs(ship_pos_x)+abs(ship_pos_y)


assert solve(test_data) == 286

with open('d12.txt') as f:
    print(solve(f.read()))
