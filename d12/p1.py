test_data = """F10
N3
F7
R90
F11"""


def turn(r_or_l, init_heading):
    if init_heading == 'E' and r_or_l == 'R':
        return 'S'
    if init_heading == 'E' and r_or_l == 'L':
        return 'N'
    if init_heading == 'S' and r_or_l == 'R':
        return 'W'
    if init_heading == 'S' and r_or_l == 'L':
        return 'E'
    if init_heading == 'W' and r_or_l == 'R':
        return 'N'
    if init_heading == 'W' and r_or_l == 'L':
        return 'S'
    if init_heading == 'N' and r_or_l == 'R':
        return 'E'
    if init_heading == 'N' and r_or_l == 'L':
        return 'W'


def solve(data):
    head_map = {
        'E': (1, 0),
        'N': (0, 1),
        'W': (-1, 0),
        'S': (0, -1),
    }
    pox_x = 0
    pox_y = 0
    heading = 'E'
    for line in data.split('\n'):
        if 'F' in line:
            delta_x = int(line[1:])*head_map[heading][0]
            delta_y = int(line[1:])*head_map[heading][1]
            pox_x += delta_x
            pox_y += delta_y
        elif 'R' in line or 'L' in line:
            for _ in range(int(line[1:])//90):
                heading = turn(line[0], heading)
        elif line[0] in ['N', 'E', 'S', 'W']:
            delta_x = int(line[1:]) * head_map[line[0]][0]
            delta_y = int(line[1:]) * head_map[line[0]][1]
            pox_x += delta_x
            pox_y += delta_y
    return abs(pox_x)+abs(pox_y)


assert solve(test_data) == 25

with open('d12.txt') as f:
    print(solve(f.read()))
